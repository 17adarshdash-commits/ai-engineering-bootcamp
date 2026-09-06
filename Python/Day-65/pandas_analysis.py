import pandas as pd

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Sneha", "Riya"],
    "Marks": [85, 72, 91, 64, 78, 88],
    "Age": [20, 21, 20, 22, 21, 20],
    "Department": ["AI", "CSE", "AI", "CSE", "AI", "CSE"]
}

df = pd.DataFrame(data)

print("Department counts:")
print(df["Department"].value_counts())

print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

print("\nDepartment statistics:")
print(df.groupby("Department")["Marks"].agg(["mean", "max", "min"]))

print("\nStudents with marks >= 80:")
print(df[df["Marks"] >= 80])

print("\nSorted by marks:")
print(df.sort_values("Marks", ascending=False))

print("\nCorrelation:")
print(df[["Marks", "Age"]].corr())
