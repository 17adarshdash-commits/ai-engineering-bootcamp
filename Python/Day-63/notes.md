# Day 63 — Pandas Foundations

## 1. What is Pandas?

Pandas is a library built on top of NumPy for working with **structured,
tabular data** — think spreadsheets or SQL tables, not just raw numbers.
It adds labeled rows and columns, mixed data types per column, and a huge
set of convenience methods for loading, cleaning, filtering, and
summarizing data. It's the standard tool for data wrangling before
feeding data into ML models.

## 2. Series

A `Series` is a one-dimensional labeled array — essentially a single
column. It has values plus an index (labels for each value).

```python
s = pd.Series([85, 72, 91, 64, 78])
```

## 3. DataFrame

A `DataFrame` is a two-dimensional labeled table — a collection of
Series that share the same index, each one a column. It's the main
Pandas data structure, built from things like dicts, lists, or CSV
files.

## 4. Creating a DataFrame

The simplest way is from a dict where keys become column names and
values become the column data:

```python
data = {"Name": ["Adarsh", "Rahul"], "Marks": [85, 72]}
df = pd.DataFrame(data)
```

## 5. head() / tail()

- `df.head(n)` → first `n` rows (default 5). Good for a quick peek at
  the start of the data.
- `df.tail(n)` → last `n` rows. Good for checking the end of the data.

## 6. info()

`df.info()` prints a summary of the DataFrame: number of rows, column
names, non-null counts per column, and each column's dtype. Useful for
spotting missing values or wrong types at a glance.

## 7. describe()

`df.describe()` computes summary statistics (count, mean, std, min,
quartiles, max) for numeric columns. Quick way to understand the
distribution of the data.

## 8. loc

`df.loc[]` selects rows/columns by **label**. Example: `df.loc[0,
"Name"]` gets the "Name" value at index label `0`. Ranges with `loc` are
inclusive on both ends.

## 9. iloc

`df.iloc[]` selects rows/columns by **integer position**, like list
indexing. Example: `df.iloc[0, 0]` gets the value at row 0, column 0.
Ranges with `iloc` are exclusive at the end, like normal Python slicing.

## 10. Filtering

You filter rows with a boolean condition inside `[]`:

```python
df[df["Marks"] > 80]
```

This builds a boolean Series (`True`/`False` per row) and keeps only the
rows where it's `True`.

## 11. mean()

`df["col"].mean()` returns the average of a numeric column.

## 12. max() / min()

`df["col"].max()` / `df["col"].min()` return the largest / smallest
value in a numeric column.

## NumPy vs Pandas

- **NumPy** → fast, homogeneous **numerical arrays** (`ndarray`). Great
  for math-heavy operations on raw numbers.
- **Pandas** → **tabular/structured data** (`DataFrame`/`Series`) with
  labeled rows/columns and mixed types per column. Great for loading,
  cleaning, filtering, and summarizing real-world datasets. Pandas is
  built on top of NumPy under the hood.
