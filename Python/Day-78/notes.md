# Day 78 — Random Forest

## Ensemble learning
Combining predictions from multiple models instead of relying on a single one. The idea is that a group of models, each with different strengths and weaknesses, tends to make better decisions together than any one model alone.

## Random Forest
A Random Forest is an ensemble of many Decision Trees. Each tree is trained slightly differently (different subsets of data/features), so they don't all make the same mistakes.

```
Decision Tree
      ↓
Multiple Decision Trees
      ↓
Random Forest
      ↓
Combined predictions
```

## Why multiple trees can help
A single Decision Tree can overfit — it can latch onto quirks in the training data and not generalize well. By averaging/voting across many trees trained on different slices of data, the errors of individual trees tend to cancel out, giving a more robust overall prediction.

## Majority voting
For classification, each tree makes its own prediction, and the Random Forest picks the class that the most trees agree on.

```
Tree 1 → Class 1
Tree 2 → Class 1
Tree 3 → Class 0
Tree 4 → Class 1
Tree 5 → Class 1

Final → Class 1
```

## RandomForestClassifier
The scikit-learn class used for classification tasks with a Random Forest. Trained the same way as any other sklearn model: `.fit(X_train, y_train)` then `.predict(X_test)`.

## n_estimators
The number of decision trees in the forest. More trees generally means more stable predictions, at the cost of more computation. Example: `n_estimators=100` builds 100 trees.

## max_depth
Limits how deep each individual tree can grow. Shallower trees are simpler and less likely to overfit; deeper trees can capture more detail but risk memorizing the training data.

## Overfitting
When a model learns the training data too closely (including its noise/quirks) and performs worse on new, unseen data. A single deep Decision Tree overfits easily. Random Forests reduce this risk because no single tree's mistakes dominate the final prediction.

---

A Random Forest combines predictions from multiple decision trees to produce a final prediction.
