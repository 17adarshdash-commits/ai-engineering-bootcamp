# Day 77 — Decision Trees: Regression

## Decision Tree Regression

A regression tree is a decision tree used to predict a **continuous number**
instead of a category. It works by splitting the data into regions (based on
feature values) and predicting a numerical value for each final region
(leaf) — usually the **average** of the target values that fall into that
leaf.

Example: instead of predicting "Pass" or "Fail", a regression tree predicts
something like "72.5" for an exam score.

## DecisionTreeRegressor

`DecisionTreeRegressor` is scikit-learn's class for building a regression
tree.

```python
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

- `model.fit(X_train, y_train)` — trains the tree by finding splits that
  group similar target values together.
- `model.predict(X_test)` — walks each test row down the tree and returns
  the average value stored at the leaf it lands on.

## Classification vs Regression

| | Classification | Regression |
|---|---|---|
| Output | Class/category | Numerical value |
| Example | Pass/Fail | Exam score |
| sklearn class | `DecisionTreeClassifier` | `DecisionTreeRegressor` |

The tree-building idea is the same (keep splitting data into purer groups),
but:
- Classification trees predict the **majority class** in a leaf.
- Regression trees predict the **average value** in a leaf.

## max_depth

`max_depth` limits how many times the tree is allowed to split.

- Small `max_depth` → simpler tree, fewer splits, more general predictions.
- Large `max_depth` → more splits, tree can fit the training data very
  closely (including its noise).

## Overfitting

Overfitting happens when the tree grows deep enough to memorize the
training data instead of learning the general trend. Signs of overfitting:

- Training error is very low, but test error is high.
- The model predicts oddly specific values for inputs that are only
  slightly different from training points.

Controlling `max_depth` (or other constraints like `min_samples_leaf`) helps
prevent overfitting.

## MAE (Mean Absolute Error)

The average of the absolute differences between actual and predicted
values.

```
MAE = average(|actual - predicted|)
```

- Same units as the target (e.g., score points).
- Lower is better. Easy to interpret: "on average, predictions are off by
  X."

## R² (R-squared / Coefficient of Determination)

Measures how much of the variance in the target the model explains,
compared to just predicting the mean every time.

- R² = 1 → perfect predictions.
- R² = 0 → model is no better than predicting the average.
- R² can be negative if the model performs worse than predicting the
  average.

## Summary Comparison

| | Classification | Regression |
|---|---|---|
| Output | Class/category | Numerical value |
| Example | Pass/Fail | Exam score |
| sklearn | `DecisionTreeClassifier` | `DecisionTreeRegressor` |
