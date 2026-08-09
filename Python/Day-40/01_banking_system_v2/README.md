# Banking System V2

A command-line banking system built as a multi-module Python package,
demonstrating module/package organization, custom exceptions, validation
helpers, and JSON persistence.

## Project Structure

```
01_banking_system_v2/
├── account.py       # Account data class (to_dict/from_dict for JSON)
├── bank.py          # Bank - account creation, deposit/withdraw/transfer, search, persistence
├── exceptions.py    # Custom exception hierarchy
├── main.py          # CLI entry point
├── accounts.json    # Default data file
└── README.md
```

## Account Fields

- Account Number
- Account Holder
- Balance
- Account Type (`Savings` / `Current`)
- Opening Date (`YYYY-MM-DD`)

## Features

- Create Account
- Deposit
- Withdraw
- Transfer Between Accounts
- Search Account (by account number, holder name, or type)
- Display Accounts
- Save to JSON
- Load from JSON

## Validation

- Account numbers must be unique (`DuplicateAccountError`)
- Account holder name cannot be empty (`InvalidAccountHolderError`)
- Account type must be `Savings` or `Current` (`InvalidAccountTypeError`)
- Opening date must match `YYYY-MM-DD` (`InvalidOpeningDateError`)
- Deposit/withdraw/transfer amounts must be a positive number (`InvalidAmountError`)
- Withdrawals and transfers cannot exceed the available balance (`InsufficientFundsError`)
- Operating on a missing account number raises `AccountNotFoundError`

All custom exceptions derive from a common `BankError` base, so the CLI
can catch a single exception type for user-facing error messages.

## Usage

```bash
cd 01_banking_system_v2
python main.py
```

Follow the on-screen menu to create accounts, deposit, withdraw, transfer
between accounts, search, display all accounts, and save/load data
to/from JSON.
