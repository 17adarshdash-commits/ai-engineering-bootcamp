"""
Day 74 — Logistic Regression (Classification)

Goal: predict a class (Pass / Fail) instead of a continuous number,
using scikit-learn's LogisticRegression.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "Hours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Pass":  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", predictions)

print("Accuracy:", accuracy_score(y_test, predictions))

print("\nProbability of classes:")
print(model.predict_proba(X_test))

print("\nPrediction for 6 hours:")
print(model.predict([[6]]))
