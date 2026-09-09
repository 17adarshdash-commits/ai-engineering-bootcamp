# Day 69 — Exploratory Data Analysis (EDA) Notes

## What is EDA?
Exploratory Data Analysis (EDA) is the process of examining a dataset to
understand its structure, content, and quality before doing any modeling.
It involves looking at the shape of the data, its types, missing values,
statistical summaries, and visualizations to get a feel for what the data
looks like and what it's telling us.

## Why EDA is important
EDA helps us understand the data before applying machine-learning algorithms.
Without it, we risk feeding a model:
- The wrong data types (e.g., numbers stored as text)
- Missing or incomplete values that break training
- Outliers or unusual values that distort results
- Imbalanced groups/categories that bias the model

EDA lets us catch these issues early, choose the right preprocessing steps,
and pick features that actually matter.

## df.shape
Returns a tuple `(rows, columns)` — tells us how big the dataset is.
Example: `(6, 4)` means 6 rows and 4 columns.

## df.columns
Lists the column names in the DataFrame. Useful for quickly seeing what
fields/features are available.

## df.dtypes
Shows the data type of each column (int64, float64, object, etc.).
Important because ML models need numeric types — text/object columns
usually need to be encoded first.

## df.head()
Displays the first few rows (default 5) of the DataFrame. A quick sanity
check to see what the actual data values look like.

## Missing values (df.isnull().sum())
`isnull()` marks each cell as True/False depending on whether it's missing.
`.sum()` adds these up per column, giving a count of missing values.
Missing data must be handled (dropped or filled) before training a model.

## df.describe()
Gives summary statistics for numeric columns: count, mean, std, min,
max, and quartiles (25%, 50%, 75%). Helps spot ranges, spread, and
potential outliers at a glance.

## groupby()
Groups rows by a category (e.g., Department) and lets us aggregate values
within each group (e.g., mean Marks per Department). Great for comparing
subgroups within the data.

## Histogram
A chart showing the distribution of a numeric column by bucketing values
into bins and counting how many fall into each bin. Helps visualize the
shape of the data (skewed, normal, bimodal, etc.) and spot unusual values.

## Summary
EDA helps us understand the data before applying machine-learning algorithms.
