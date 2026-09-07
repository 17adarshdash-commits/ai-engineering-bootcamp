# Day 67 — Data Visualization Practice

## DataFrame.plot()
A convenience method built into Pandas that wraps Matplotlib. Instead of manually
pulling columns out and calling `plt.plot(...)`, you can call `.plot()` directly
on a DataFrame/Series and just tell it which columns to use (`x=`, `y=`) and
what kind of chart to draw (`kind=`). Under the hood it's still Matplotlib, so
`plt.title()`, `plt.xlabel()`, `plt.show()`, etc. all work as normal afterward.

## Line chart
Connects data points with a line, in order. Best for showing how a value
changes over a continuous sequence — usually time (days, months, years).
Used today for the Sales trend across months.

## Bar chart
Draws a separate bar per category. Best for comparing discrete/categorical
values side by side (e.g., Sales per month as separate bars) rather than
implying a continuous flow between them like a line chart does.

## Scatter plot
Plots individual points using two numeric columns, one on each axis (no
connecting line). Best for seeing whether two variables move together —
i.e., checking for a relationship/correlation between them. Used today for
Sales vs Customers.

## When to use each
- **Line** → tracking one variable over time / an ordered sequence, to see trend and direction.
- **Bar** → comparing sizes across separate categories at a glance.
- **Scatter** → checking if two numeric variables are related to each other.

## What a trend means
A trend is the general direction a value moves over time — upward, downward,
or flat — even if there are small dips or spikes along the way. It's the
"big picture" pattern, not every individual fluctuation.

## What a relationship/correlation means
A relationship (or correlation) is when two variables tend to change together —
e.g., as one goes up, the other tends to go up too (positive relationship), or
one goes up while the other goes down (negative relationship). A scatter plot
makes this visible: if the points roughly trend upward left-to-right, that's a
positive relationship. It does **not** by itself prove one variable *causes*
the other to change — just that they move together.

## Takeaway
Visualization helps us discover patterns that may be difficult to see from raw numbers.
