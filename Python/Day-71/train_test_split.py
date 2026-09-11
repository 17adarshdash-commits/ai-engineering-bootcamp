import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 72, 75, 80, 82, 85, 90, 95],
    "Score": [40, 45, 50, 55, 60, 68, 72, 78, 85, 92]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training features:")
print(X_train)

print("\nTesting features:")
print(X_test)

print("\nTraining targets:")
print(y_train)

print("\nTesting targets:")
print(y_test)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))
