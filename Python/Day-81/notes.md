# Day 81 — KNN: Choosing K

## What is a hyperparameter?
A hyperparameter is a setting you choose before training that controls how
the model learns, rather than something the model learns from data itself
(like weights or coefficients). K is a hyperparameter that controls how
many neighboring points KNN considers when making a prediction.

## What happens when K is too small?
With a very small K (e.g. K=1), the prediction depends on just one or a
few nearby points. The model becomes extremely sensitive to individual
training points, including noise and outliers. This leads to overfitting —
great accuracy on training data, but shaky generalization to new data.

## What happens when K is too large?
With a very large K, the model considers too many neighbors, including
points that aren't really "close" or relevant. The decision boundary
becomes too smooth/generic and the model can underfit, failing to capture
real patterns in the data.

## What is overfitting?
Overfitting is when a model learns the training data too closely —
including its noise and quirks — so it performs well on training data but
poorly on new, unseen data.

## What is underfitting?
Underfitting is when a model is too simple or too generalized to capture
the actual pattern in the data, so it performs poorly on both training and
test data.

## Why is choosing K important?
K controls the overfitting/underfitting tradeoff. A good K balances
sensitivity to local patterns (low K) against stability/generalization
(high K). It's usually chosen by testing several K values and comparing
performance on a validation set.

## Experiment observation
Ran K = 1, 3, 5, 7 on the small Hours/Attendance dataset from Day 80.
All K values gave 100% accuracy — expected, since the dataset is tiny and
the classes are cleanly separated (low hours/attendance = fail, high =
pass). With a dataset this small and clean, differences between K values
don't really show up. The point was understanding the *effect* of K, not
getting a production-quality result.
