# Day 72 — Linear Regression + DSA

## The ML workflow

```
Data
 ↓
Features (X) + Target (y)
 ↓
Train/Test Split
 ↓
Linear Regression
 ↓
Fit Model
 ↓
Predict
 ↓
Evaluate
```

## Linear Regression
An algorithm that models the relationship between input(s) and a
continuous numerical output as a straight line:

```
y = mx + b
```

Given `Hours` studied, it tries to draw the line that best predicts
`Score`. `m` is the slope (how much `y` changes per unit of `x`), and
`b` is where the line crosses the y-axis.

Linear Regression learns a relationship between input features and a
continuous numerical target.

## Feature
An input column the model uses to make a prediction. In today's
example: `Hours`.

## Target
The output/answer the model is trying to predict — must be a
continuous number for Linear Regression (not a category). In today's
example: `Score`.

## Independent vs dependent variable
- **Independent variable** — the input, i.e. the feature (`Hours`).
  It doesn't depend on anything else in the model.
- **Dependent variable** — the output, i.e. the target (`Score`). Its
  value depends on the independent variable(s).

## Best-fit line
Out of all possible straight lines that could be drawn through the
data, the "best-fit" line is the one that minimizes the overall
distance between the line and the actual data points. Linear
Regression's job is to find this line's slope and intercept.

## `fit()`
Trains the model. `model.fit(X_train, y_train)` shows the model the
training features and their correct answers, and it calculates the
best `m` (coefficient) and `b` (intercept) from that data.

## `predict()`
Uses the trained model to estimate the target for new/unseen inputs.
`model.predict(X_test)` returns the model's guesses for the test set.

## MSE (Mean Squared Error)
The average of the squared differences between actual and predicted
values. Squaring punishes bigger mistakes more heavily. Lower MSE =
better fit. It's in squared units of the target, so it's more useful
for comparing models than for standalone interpretation.

## R² score
Measures how much of the variation in the target the model explains,
on a scale that tops out at 1.0:
- `1.0` → the model perfectly explains the target
- `0.0` → the model does no better than just predicting the average
- negative → the model does worse than predicting the average

`r2_score(y_test, predictions)` gives this value for the test set.

## Coefficient
`model.coef_` — the learned slope(s) (`m`). It tells you how much the
target is expected to change for a one-unit increase in the feature.
E.g. if the coefficient is ~6, each extra hour studied predicts
roughly 6 more points on the score.

## Intercept
`model.intercept_` — the learned `b`, i.e. the predicted target value
when all features are 0. It's where the best-fit line crosses the
y-axis.

## Key takeaway
Linear Regression learns a relationship between input features and a
continuous numerical target.
