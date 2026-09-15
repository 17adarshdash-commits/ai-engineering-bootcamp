# Day 74 — Logistic Regression

## From regression to classification
- **Linear Regression** → predicts a *number* (e.g. price, score).
- **Logistic Regression** → predicts a *class* (e.g. Pass/Fail, Spam/Not Spam).

## Classification
A supervised learning task where the model assigns each input to one
of a fixed set of categories instead of a continuous value.

## Binary classification
Classification with exactly two possible classes, usually labeled
`0` and `1` (e.g. Fail/Pass, No/Yes).

## Logistic Regression
Despite the name "regression," it's a classification algorithm.
Internally it estimates the **probability** that a sample belongs to
class `1`, then converts that probability into a class label using a
threshold. (The sigmoid function is what squashes the raw output into
a 0–1 probability — the math isn't the focus today, just the intuition.)

## Probability output
Instead of jumping straight to "Pass" or "Fail," the model first
outputs something like "78% chance of Pass." This is more informative
than a bare label — it tells you how confident the model is.

## Decision threshold
The cutoff probability used to convert a probability into a class.
By default it's `0.5`:
- probability ≥ 0.5 → class 1
- probability < 0.5 → class 0

The threshold can be moved (e.g. to 0.7) to make the model more or
less conservative about predicting class 1.

## fit()
`model.fit(X_train, y_train)` — trains the classifier by finding the
parameters that best separate the classes in the training data.

## predict()
`model.predict(X_test)` — returns the predicted class label (0 or 1)
for each sample, after applying the decision threshold.

## predict_proba()
`model.predict_proba(X_test)` — returns the underlying probabilities
for each class, e.g. `[[0.12, 0.88]]` means 12% Fail, 88% Pass.
`predict()` is really just `predict_proba()` + a threshold.

## Accuracy
The fraction of predictions that match the actual labels:
`accuracy = correct predictions / total predictions`.
Simple and intuitive, but can be misleading on imbalanced datasets
(e.g. 95% accuracy is meaningless if 95% of samples are class 0).

---

Logistic Regression is commonly used for classification problems
where the output represents a class.
