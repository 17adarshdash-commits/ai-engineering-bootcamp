import pandas as pd

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Rahul"],
    "Marks": [85, None, 91, 64, None],
    "Age": [20, 21, None, 22, 21]
}

df = pd.DataFrame(data)

print("Original:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

print("\nAfter filling missing marks:")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)

print("\nAfter filling missing age:")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print("\nAfter removing duplicates:")
df = df.drop_duplicates()
print(df)

print("\nSorted by marks:")
print(df.sort_values("Marks", ascending=False))
