import numpy as np
import pandas as pd

data = {
    "Name": ["Adarsh", "Rahul", "Priya", "Aman", "Sneha"],
    "Marks": [85, 72, 91, 64, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Convert column to NumPy array
marks = df["Marks"].to_numpy()

print("\nNumPy array:")
print(marks)

print("\nMean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# Create a calculated column
df["Bonus"] = 5
df["Updated Marks"] = df["Marks"] + df["Bonus"]

print("\nUpdated DataFrame:")
print(df)

# Normalize marks
df["Normalized"] = df["Marks"] / np.max(df["Marks"])

print("\nNormalized marks:")
print(df)
