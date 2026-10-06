import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
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

scaler = StandardScaler()

# Fit the scaler only on training data, then apply that same transform to
# the test set. Fitting on X_test too would leak test-set statistics (its
# mean/std) into the model's preprocessing, giving an overly optimistic
# evaluation of how the model performs on unseen data.
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print("Predictions:", predictions)
print("Actual:", y_test.values)
print("Accuracy:", accuracy_score(y_test, predictions))
