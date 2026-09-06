# Day 65 — Pandas Data Analysis

## `value_counts()`
Counts how many times each unique value appears in a column, sorted
descending by default. Great for a first look at a categorical column —
e.g. `df["Department"].value_counts()` immediately shows the class balance
(how many AI vs CSE students).

## `groupby()`
Splits the DataFrame into groups based on the values in a column, so any
operation applied afterward runs separately per group instead of over the
whole dataset. On its own it just returns a groupby object — it needs a
column selection and an aggregation to produce a result, e.g.
`df.groupby("Department")["Marks"].mean()`.

Think of it as: **split → select column → apply function**, run once per
group.

## `agg()`
Applies one or more aggregation functions at once instead of chaining
separate calls. `df.groupby("Department")["Marks"].agg(["mean", "max", "min"])`
returns a table with all three stats per group in one shot, which is faster
to read than calling `.mean()`, `.max()`, `.min()` separately.

## Conditional filtering
Selecting rows based on a boolean condition, e.g. `df[df["Marks"] >= 80]`.
`df["Marks"] >= 80` produces a Series of True/False (one per row), and
indexing the DataFrame with that Series keeps only the rows marked True.
Multiple conditions combine with `&` (and) / `|` (or), each wrapped in
parentheses.

## `sort_values()`
Sorts the DataFrame by one or more columns. `df.sort_values("Marks",
ascending=False)` puts the highest scorers first — useful for ranking and
for spotting top/bottom performers at a glance.

## `corr()`
Computes the pairwise correlation coefficient (Pearson by default) between
numeric columns, ranging from -1 to 1. A value near 1 means the columns
tend to increase together, near -1 means one increases as the other
decreases, and near 0 means little linear relationship. `df[["Marks",
"Age"]].corr()` checks whether marks and age move together in this dataset.

## Why grouping is useful in data analysis
Raw rows rarely answer the real question — "how well did AI students do
compared to CSE?" needs the data split by department first. Grouping turns
a flat table into per-category summaries, which is exactly the kind of
pattern (averages, counts, spread per segment) that reveals trends and
feeds into feature engineering for ML.

## Example — `groupby()` in my own words
`df.groupby("Department")["Marks"].mean()` takes all the students, splits
them into an "AI" bucket and a "CSE" bucket based on their Department, keeps
only the Marks column for each bucket, and then averages the marks within
each bucket separately. The result is one average per department instead of
one average for everyone mixed together.
