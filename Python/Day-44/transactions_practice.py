"""
transactions_practice.py

Creates two bank accounts in SQLite and implements transfer_money(),
which withdraws from one account and deposits into another inside a
single transaction - committing only if both steps succeed, and rolling
back the whole thing if either step fails. Demonstrates both a
successful transfer and a failed transfer.
"""

import sqlite3

CREATE_ACCOUNTS_SQL = """
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner TEXT NOT NULL,
    balance REAL NOT NULL CHECK (balance >= 0)
)
"""

ACCOUNTS = [
    (1, "Alice", 500.0),
    (2, "Bob", 100.0),
]


class InsufficientFundsError(Exception):
    """Raised when a transfer would leave the sender's balance negative."""


def setup(conn):
    """Create the accounts table and seed it with two starting balances."""
    conn.execute(CREATE_ACCOUNTS_SQL)
    conn.executemany(
        "INSERT INTO accounts (account_id, owner, balance) VALUES (?, ?, ?)",
        ACCOUNTS,
    )
    conn.commit()


def get_balance(conn, account_id):
    cursor = conn.execute(
        "SELECT balance FROM accounts WHERE account_id = ?", (account_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else None


def transfer_money(conn, from_account, to_account, amount):
    """
    Transfer `amount` from `from_account` to `to_account` as a single
    transaction: withdraw, then deposit, then commit. If either step
    fails (insufficient funds, a bad account id, or a CHECK constraint
    violation), roll back so neither side of the transfer is applied.
    """
    try:
        # Begin a transaction - withdraw from the sender first.
        sender_balance = get_balance(conn, from_account)
        if sender_balance is None:
            raise ValueError(f"Account {from_account} does not exist.")
        if sender_balance < amount:
            raise InsufficientFundsError(
                f"Account {from_account} has {sender_balance:.2f}, "
                f"cannot withdraw {amount:.2f}."
            )

        conn.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_id = ?",
            (amount, from_account),
        )

        # Deposit into the receiver.
        cursor = conn.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
            (amount, to_account),
        )
        if cursor.rowcount == 0:
            raise ValueError(f"Account {to_account} does not exist.")

        conn.commit()
        print(f"Transferred {amount:.2f} from {from_account} to {to_account}.")
    except (InsufficientFundsError, ValueError, sqlite3.IntegrityError) as e:
        conn.rollback()
        print(f"Transfer failed and rolled back: {e}")


def print_balances(conn):
    cursor = conn.execute("SELECT account_id, owner, balance FROM accounts ORDER BY account_id")
    print("\n-- Account balances --")
    for account_id, owner, balance in cursor.fetchall():
        print(f"Account {account_id} ({owner}): {balance:.2f}")


def main():
    conn = sqlite3.connect(":memory:")
    try:
        setup(conn)
        print_balances(conn)

        # Successful transfer: Alice has enough funds.
        transfer_money(conn, from_account=1, to_account=2, amount=200.0)
        print_balances(conn)

        # Failed transfer: Bob no longer has enough to send 500 - the
        # withdrawal never gets applied because the whole transaction rolls
        # back before commit() is reached.
        transfer_money(conn, from_account=2, to_account=1, amount=500.0)
        print_balances(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
