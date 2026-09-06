# Day 66 — Pandas + Matplotlib Foundations + DSA

## Matplotlib

Matplotlib is Python's core plotting library. It takes numbers (often
from a Pandas Series/DataFrame) and turns them into visuals — line
plots, bar charts, scatter plots, histograms, etc. It's usually
imported as:

```python
import matplotlib.pyplot as plt
```

### Line plot
`plt.plot(x, y)` — connects data points with a line, in order. Best
for showing a trend over a continuous sequence, like time (e.g. stock
price over days, temperature over months).

### Bar chart
`plt.bar(x, y)` — draws a bar per category, height = value. Best for
**comparing discrete categories** against each other (e.g. marks per
student, sales per product).

### Scatter plot
`plt.scatter(x, y)` — plots each point individually with no
connecting line. Best for showing the **relationship or spread**
between two numerical variables (e.g. hours studied vs marks scored),
and for spotting clusters or outliers.

### `xlabel()`
`plt.xlabel("label")` — labels the x-axis so the reader knows what
the horizontal values represent.

### `ylabel()`
`plt.ylabel("label")` — labels the y-axis so the reader knows what
the vertical values represent.

### `title()`
`plt.title("title")` — sets the title displayed above the chart,
summarizing what the plot shows.

### `legend()`
`plt.legend()` — displays a key mapping each plotted series/label to
its color or marker, useful when multiple lines/series share a chart.

### `show()`
`plt.show()` — renders and displays the figure in a window (or inline
in notebooks). Without it, the plot is built in memory but never
shown.

## Pandas vs Matplotlib

- **Pandas** → data manipulation / analysis. Loading, cleaning,
  filtering, grouping, and computing statistics on data
  (DataFrames/Series).
- **Matplotlib** → data visualization. Takes the numbers Pandas
  produced and turns them into charts so patterns are visible at a
  glance.

Together: Pandas tells you **what** is happening in the data,
Matplotlib helps you **see** it.

## DSA Review — LeetCode 121: Best Time to Buy and Sell Stock

**Problem:** Given daily stock prices, find the max profit from one
buy + one later sell.

**Key idea:**
```
minimum price so far
        ↓
current possible profit (price - min_so_far)
        ↓
maximum profit (running max of the above)
```

Single left-to-right pass, tracking:
- `min_price_so_far` — lowest price seen up to (and including) today
- `max_profit_so_far` — best profit achievable if sold today

**Complexity:**
- Time: O(n)
- Space: O(1)

### Challenge — why not compare every buy/sell pair?

Brute force checks every pair `(buy_day, sell_day)` with
`buy_day < sell_day`, which is O(n²). But for any fixed sell day, the
most profitable buy day is always the one with the **lowest price
seen so far** — no other earlier day could beat it, since profit is
just `sell_price - buy_price` and we want to minimize the price we
paid. So instead of re-scanning all prior days for every sell day, we
carry forward a single running minimum. That turns the inner loop
into O(1) work per day, collapsing the whole algorithm to O(n).
