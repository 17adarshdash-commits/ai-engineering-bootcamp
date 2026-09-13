# Day 73 — Linear Regression Evaluation

## The evaluation workflow

```
Model
   ↓
Predictions
   ↓
Compare predictions vs actual values
   ↓
MSE / MAE / R²
   ↓
Interpret performance
```

## Prediction error
The difference between what the model predicted and what actually
happened: `error = actual - predicted`. Every metric below is just a
different way of summarizing these errors across all test samples.

## MAE — Mean Absolute Error
The average of the absolute value of every prediction error. It answers
"on average, how far off is the model?" in the same units as the
target (e.g. score points). Because it uses absolute values, big and
small errors are weighted proportionally — no extra penalty for large
misses.

## MSE — Mean Squared Error
The average of the *squared* prediction errors. Squaring makes every
error positive and punishes large errors much more than small ones
(an error of 10 contributes 100, not 10). Useful when big mistakes are
especially costly, but harder to interpret directly since the units
are squared (e.g. score points²).

## R² Score
Measures how much of the variation in the target the model explains,
relative to just guessing the average every time.
- `R² = 1` → perfect fit
- `R² = 0` → model does no better than predicting the mean
- `R² < 0` → model is worse than just guessing the mean

## Why we evaluate on test data
The model already saw the training data while fitting itself, so
scoring it there just measures memorization, not real skill. The test
set is unseen data — evaluating on it tells us how the model is likely
to perform on new, real-world inputs.

## Lower vs higher — which way is "good"?

| Metric | Better Direction |
|--------|-------------------|
| MAE    | Lower             |
| MSE    | Lower             |
| R²     | Higher            |

## Key takeaway
No single metric tells the whole story — MAE/MSE describe the size of
the errors, while R² describes how much of the pattern the model
actually captured. Look at all three together.
