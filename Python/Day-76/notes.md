# Day 76 — Decision Trees

## The workflow
```
                    Dataset
                       ↓
                 Best question?
                  /          \
                Yes           No
                ↓              ↓
             Split           Split
              ↓                ↓
          More decisions → Final prediction
```
A Decision Tree makes predictions by repeatedly splitting data based on
feature values.

## Decision Tree
A model that predicts an outcome by asking a series of yes/no questions
about the features, narrowing down the data at each step until it
reaches an answer. No coefficients or equations like Linear/Logistic
Regression — just a sequence of splits.

## Root node
The very first question, at the top of the tree. It looks at the whole
dataset and picks the feature (and threshold) that best separates the
classes.

## Decision node (internal node)
Any node after the root that still asks another question and splits
the data further. A tree can have many of these, one per remaining
question.

## Branch
The path leading out of a node based on the answer to its question
(e.g. the "Yes" arrow or the "No" arrow in the diagram above).

## Leaf node
A node at the bottom of the tree that no longer splits — it just gives
the final prediction (a class label for classification, a number for
regression).

## Splitting
The process of dividing data at a node into two (or more) groups based
on a feature test, like `Temperature > 25?`. The tree picks the split
that makes each resulting group as "pure" (single-class) as possible.

## Gini impurity
A measure of how mixed the classes are within a node. A node with only
one class has zero impurity (perfectly pure); a node with an even mix
of classes has high impurity. The tree chooses splits that reduce
impurity the most — don't worry about calculating it by hand, just
know it's the "how mixed is this group?" score the tree optimizes.

## max_depth
A limit on how many levels of questions the tree is allowed to ask
before it must stop and predict. Smaller `max_depth` = simpler tree;
larger `max_depth` = more splits and more complexity.

## Overfitting
When a tree grows so deep it starts memorizing quirks of the training
data (down to individual data points) instead of learning general
patterns. It looks great on training data but performs poorly on new,
unseen data. `max_depth` (and other limits) help control this by
forcing the tree to stay simpler.

## Classification tree vs regression tree
- **Classification tree**: leaves predict a category/class (e.g. Pass
  or Fail). Splits are chosen to reduce impurity (like Gini).
- **Regression tree**: leaves predict a continuous number (e.g. a
  price). Splits are chosen to reduce variance/error in each group.

## DecisionTreeClassifier
```python
DecisionTreeClassifier(max_depth=3, random_state=42)
```
Creates a classification tree model, capped at 3 levels of questions,
with a fixed random seed for reproducible results.

```python
model.fit(X_train, y_train)
```
Trains the tree — it examines the training data and figures out the
best feature/threshold to split on at each node.

```python
model.predict(X_test)
```
Runs new data down the trained tree, following the Yes/No branches at
each node, until it lands on a leaf and returns that leaf's prediction.

## Worked example (from decision_tree.py)
Dataset of study Hours + Attendance % predicting Pass (0/1). With
`max_depth=3`, the tree finds thresholds like "Hours > some value" or
"Attendance > some value" to separate passers from non-passers.

On the held-out test split, the model predicted both test rows
correctly (Accuracy: 1.0) — unsurprising since this toy dataset is
cleanly separable (low hours/attendance → 0, high hours/attendance →
1). For a student with 6 hours studied and 80% attendance, the model
predicts **Pass (1)**.
