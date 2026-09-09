import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Sneha", "Riya"],
    "Marks": [85, 72, 91, 64, 78, 88],
    "Age": [20, 21, 20, 22, 21, 20],
    "Department": ["AI", "CSE", "AI", "CSE", "AI", "CSE"]
}

df = pd.DataFrame(data)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nFirst rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

df["Marks"].plot(kind="hist", bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.show()
