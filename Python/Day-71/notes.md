# Day 71 — Train/Test Split + ML Workflow

## The ML workflow

```
Dataset
   ↓
Features (X) + Target (y)
   ↓
Train / Test Split
   ↓
Train Model
   ↓
Make Predictions
   ↓
Evaluate Model
```

## Training data
The portion of the dataset the model actually learns from. The model looks
at these examples and adjusts itself to find patterns between the inputs
(X) and the correct outputs (y).

## Testing data
Data the model never saw during training. It's used afterward to check
how well the model generalizes — i.e., how it performs on new, unseen
examples instead of the ones it memorized.

## Why we split
If we evaluate a model only on data it already trained on, the score is
misleading — the model could just be memorizing rather than learning a
real pattern. Splitting gives a more honest, realistic measure of
performance on data the model hasn't encountered before.

## Features (X)
The input columns the model uses to make a prediction. In today's
example: `Hours_Studied` and `Attendance`.

## Target (y)
The output/answer the model is trying to predict. In today's example:
`Score`.

## `train_test_split()`
A scikit-learn function that randomly divides X and y into training and
testing subsets:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

- `X_train` → training inputs
- `X_test`  → testing inputs
- `y_train` → training answers
- `y_test`  → testing answers

## `test_size`
Fraction of the data set aside for testing. `test_size=0.2` means 20%
of the rows go to the test set, and the remaining 80% go to training.
For our 10-row dataset, that's 8 training samples and 2 testing samples.

## `random_state`
A seed value that makes the "random" split reproducible. Using the same
`random_state` (e.g. 42) means every run produces the exact same split,
which is useful for consistent, comparable results.

## Key takeaway
The test set should represent unseen data that the model did not train on.
