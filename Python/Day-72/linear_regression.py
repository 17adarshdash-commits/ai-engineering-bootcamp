import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", predictions)

print("MSE:", mean_squared_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

print("Predicted score for 7 hours:",
      model.predict([[7]])[0])
