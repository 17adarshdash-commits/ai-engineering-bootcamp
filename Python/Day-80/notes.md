# Day 80 — KNN

## KNN (K-Nearest Neighbors)
A simple classification (or regression) algorithm with no real "training" step. To predict a new point's label, it looks at the K closest points in the training data and bases the prediction on them. It's an instance-based / lazy learner — all the work happens at prediction time.

## K
The number of neighbors the model looks at when making a prediction. Small K (e.g. 1) makes the model sensitive to noise/outliers; large K smooths predictions but can blur the boundary between classes. K is usually chosen as an odd number for binary classification to avoid ties.

## Neighbors
The K training points closest to the new point being predicted, measured by distance in feature space.

## Distance
How "close" two points are. The most common metric is Euclidean distance:

```
distance = sqrt((x1 - x2)^2 + (y1 - y2)^2 + ...)
```

KNN relies entirely on distance to decide which points count as neighbors, so the scale of each feature matters a lot.

## Majority voting
Once the K nearest neighbors are found, the predicted class is whichever label appears most often among them. Example: if 3 nearest neighbors have labels [1, 1, 0], the prediction is 1 (2 votes vs 1).

## Feature scaling
Distance-based algorithms like KNN compare raw feature values, so a feature with a larger numeric range (e.g. Attendance: 0-100) will dominate the distance calculation over a feature with a smaller range (e.g. Hours: 0-10), even if both are equally important. Scaling (e.g. StandardScaler) puts every feature on the same scale so each contributes fairly to the distance.

### Why `fit_transform` on train, `transform` on test
```python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
`fit_transform` on `X_train` computes the mean/std from the training data and applies the transform. `transform` on `X_test` reuses those same training-set statistics instead of recomputing them. If we fit a separate scaler on `X_test`, the test set's own mean/std would leak into preprocessing — information the model shouldn't have access to at evaluation time — making the accuracy estimate overly optimistic and not representative of real unseen data.

## n_neighbors
The `KNeighborsClassifier` parameter that sets K — how many nearest neighbors to use for the majority vote. `KNeighborsClassifier(n_neighbors=3)` looks at the 3 closest training points for each prediction.
