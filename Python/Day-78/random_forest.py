import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    "Hours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [55, 60, 65, 70, 72, 80, 82, 85, 90, 95],
    "Pass": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", predictions)

print("Accuracy:", accuracy_score(y_test, predictions))

print("\nPrediction for 6 hours and 80% attendance:")
print(model.predict([[6, 80]]))
