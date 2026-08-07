# Expense Tracker V2

A command-line expense tracker built as a multi-module Python package,
demonstrating module/package organization, custom exceptions, and JSON
persistence.

## Project Structure

```
expense_tracker_v2/
├── expense.py       # Expense data class (to_dict/from_dict for JSON)
├── tracker.py        # ExpenseTracker - CRUD, search, totals, persistence
├── exceptions.py     # Custom exception hierarchy
├── main.py           # CLI entry point
├── expenses.json      # Default data file
└── README.md
```

## Expense Fields

- Expense ID
- Title
- Category
- Amount
- Date (`YYYY-MM-DD`)

## Features

- Add Expense
- Update Expense
- Delete Expense
- Search Expenses (by ID, title, category, or date)
- Display Expenses
- Total Spending
- Spending by Category
- Save to JSON
- Load from JSON

## Validation

- Expense IDs must be unique (`DuplicateExpenseIDError`)
- Title cannot be empty (`InvalidTitleError`)
- Category cannot be empty (`InvalidCategoryError`)
- Amount must be a positive number (`InvalidAmountError`)
- Date must match `YYYY-MM-DD` (`InvalidDateError`)
- Operating on a missing expense ID raises `ExpenseNotFoundError`

All custom exceptions derive from a common `ExpenseError` base, so the
CLI can catch a single exception type for user-facing error messages.

## Usage

```bash
cd expense_tracker_v2
python main.py
```

Follow the on-screen menu to add, update, delete, search, and display
expenses, view totals, and save/load data to/from JSON.
