# Day 64 — Pandas Data Cleaning

## Missing values
Real-world data often has gaps — a sensor didn't record, a survey question was
skipped, a field wasn't entered. Pandas represents these gaps as `NaN` (Not a
Number). Missing values can break calculations (e.g. `mean()`) or mislead a
model if left unhandled, so they need to be found and dealt with before
analysis or training.

## `isnull()` / `isna()`
Returns a same-shaped DataFrame/Series of booleans marking which cells are
`NaN`. `df.isnull().sum()` gives a per-column count of missing values —
usually the first thing to check on a new dataset.

## `fillna()`
Fills missing values with something else — a constant, the column mean/
median, or a forward/backward fill from neighboring rows.
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```
This keeps the row instead of discarding it, at the cost of introducing an
estimated (not real) value.

## `dropna()`
Removes rows (or columns, with `axis=1`) that contain any `NaN`. Simple and
safe when missing data is rare, but wasteful if it means throwing away a lot
of otherwise-good rows.

## `drop_duplicates()`
Removes rows that are exact duplicates of an earlier row (by default, across
all columns). Duplicate rows can silently bias statistics and model training
by over-weighting repeated entries.

## `sort_values()`
Sorts the DataFrame by one or more columns, e.g.
`df.sort_values("Marks", ascending=False)`. Useful for inspecting extremes
(top/bottom performers) and for spotting outliers during cleaning.

## Why data cleaning matters before ML
Models learn whatever patterns are in the data they're given. Missing values
can crash computations or get silently mishandled, duplicates can bias the
model toward repeated examples, and inconsistent/incorrect values teach the
model the wrong patterns. Cleaning first means the model trains on an
accurate, representative picture of the data — "garbage in, garbage out"
applies directly.

## Mean imputation
Replacing missing numerical values with the column's mean. It's simple and
keeps the dataset's overall average unchanged, but it reduces variance and
can be misleading if the data isn't roughly symmetric or has outliers.
