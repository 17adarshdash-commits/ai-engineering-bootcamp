import pandas as pd

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Sneha"],
    "Marks": [85, 72, 91, 64, 78],
    "Age": [20, 21, 20, 22, 21]
}

df = pd.DataFrame(data)

print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nInformation:")
df.info()

print("\nStatistics:")
print(df.describe())

print("\nNames:")
print(df["Name"])

print("\nStudents with marks > 80:")
print(df[df["Marks"] > 80])

print("\nAverage marks:")
print(df["Marks"].mean())

print("\nHighest marks:", df["Marks"].max())
print("Lowest marks:", df["Marks"].min())

print("\nStudents aged 21 or older:")
print(df[df["Age"] >= 21])
