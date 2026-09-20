# Day 79 — Random Forest Evaluation

## Accuracy
The fraction of predictions the model got right overall: (correct predictions) / (total predictions). Simple to understand, but can be misleading on its own.

## Why accuracy isn't always sufficient
On an imbalanced dataset (e.g. 95 "Pass" and 5 "Fail"), a model that always predicts "Pass" gets 95% accuracy while being useless at catching the "Fail" cases. Accuracy hides how the model performs on each class individually — precision, recall, and F1 look at that instead.

## Precision
Of everything the model predicted as positive, how much was actually positive: TP / (TP + FP). High precision means few false alarms. Matters when a false positive is costly (e.g. flagging a good student as failing).

## Recall
Of everything that was actually positive, how much did the model catch: TP / (TP + FN). High recall means few missed cases. Matters when a false negative is costly (e.g. missing a student who will actually fail).

## F1 Score
The harmonic mean of precision and recall: 2 * (precision * recall) / (precision + recall). A single number that balances both — useful when you care about precision and recall together and don't want to pick one over the other.

## Confusion Matrix
A table comparing predicted vs actual labels:

```
                Predicted 0   Predicted 1
Actual 0        TN            FP
Actual 1        FN            TP
```

It's the source that precision, recall, and F1 are all calculated from — it shows exactly which mistakes the model is making, not just how many.

## Feature Importance
`model.feature_importances_` returns how much each feature contributed to the trees' decisions, based on how much it reduced impurity across all the splits in the forest. Example:

```
Hours       → 0.65
Attendance  → 0.35
```

```python
for feature, importance in zip(X.columns, model.feature_importances_):
    print(feature, ":", importance)
```

`zip(X.columns, model.feature_importances_)` pairs each column name with its corresponding importance score (they're in the same order), so the loop prints each feature next to how much the model relied on it.

---

Feature importance describes how useful a feature was to the trained model; it does not establish causation.
