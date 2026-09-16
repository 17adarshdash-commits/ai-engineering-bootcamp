# Day 75 — Classification Evaluation

## The workflow
```
Classification Model
       ↓
   Predictions
       ↓
Confusion Matrix
       ↓
Accuracy / Precision / Recall / F1
```
A model isn't done once it predicts labels — you need a way to check
whether those predictions were actually good.

## Confusion Matrix
A table that breaks predictions down by what actually happened vs.
what the model guessed:
```
                 Predicted
                0       1

Actual  0      TN      FP
        1      FN      TP
```
It's the raw material every other metric below is built from.

## TP — True Positive
Actual = 1, predicted = 1. The model correctly caught a positive case.

## TN — True Negative
Actual = 0, predicted = 0. The model correctly caught a negative case.

## FP — False Positive
Actual = 0, predicted = 1. A "false alarm" — the model said yes when
the real answer was no.

## FN — False Negative
Actual = 1, predicted = 0. A "miss" — the model said no when the real
answer was yes.

## Accuracy
```
(TP + TN) / (TP + TN + FP + FN)
```
Fraction of all predictions that were correct. Simple, but misleading
on imbalanced data — a model that always predicts "no disease" can
score 95% accuracy if only 5% of patients actually have it.

## Precision
```
TP / (TP + FP)
```
Of everything predicted positive, how much was actually positive?
Answers: "When the model says YES, how often is it right?"
Low precision = lots of false alarms.

## Recall
```
TP / (TP + FN)
```
Of everything that was actually positive, how much did the model
catch? Answers: "How many of the real YES cases did we find?"
Low recall = lots of missed cases.

## F1 Score
```
2 * (Precision * Recall) / (Precision + Recall)
```
The harmonic mean of precision and recall — a single number that
balances the two. Useful when you care about both and want one score
to compare models by, especially on imbalanced data.

## Worked example (from classification_metrics.py)
```
actual    = [1, 1, 0, 0, 1, 0, 1, 0]
predicted = [1, 0, 0, 0, 1, 1, 1, 0]

Confusion Matrix:
[[3 1]
 [1 3]]
```
- TN = 3 (actual 0, predicted 0)
- FP = 1 (actual 0, predicted 1)
- FN = 1 (actual 1, predicted 0)
- TP = 3 (actual 1, predicted 1)

Accuracy = Precision = Recall = F1 = 0.75 here — the dataset happens
to be small and symmetric enough that they all line up. That's not
typical; usually they diverge.

## Is accuracy alone enough?
No. Accuracy hides *what kind* of mistakes a model makes. Two models
can have identical accuracy while one racks up false positives and
the other racks up false negatives — and those failure modes often
have very different real-world costs. You need precision/recall (or
F1) to see that difference, especially on imbalanced datasets.

## When precision matters more than recall
When false positives are costly. Example: spam filter — flagging a
real email as spam (FP) is worse than letting one spam email through
(FN). You want to be *sure* before saying "positive."

## When recall matters more than precision
When false negatives are costly. Example: disease screening — missing
an actual sick patient (FN) is far worse than a false alarm that leads
to an extra test (FP). You want to catch as many real positives as
possible, even at the cost of some false alarms.
