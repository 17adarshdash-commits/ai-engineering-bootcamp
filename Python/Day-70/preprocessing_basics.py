"""
Day 70 — Data Preprocessing for ML
Pipeline: Raw Data -> Clean Data -> Select Features -> Encode Categorical Data
          -> Scale Numerical Data -> Training-ready Data
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

data = {
    "Hours_Studied": [2, 4, 6, 8, 10],
    "Department": ["CSE", "AI", "CSE", "AI", "CSE"],
    "Score": [45, 55, 65, 78, 90]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

# Encode categorical data
# LabelEncoder turns each unique category string into an integer code.
# Example: "AI" -> 0, "CSE" -> 1 (alphabetical order by default).
encoder = LabelEncoder()
df["Department"] = encoder.fit_transform(df["Department"])

print("\nEncoded data:")
print(df)

# Select features
# X = the inputs (features) the model will learn from.
# y = the output (target) the model is trying to predict.
X = df[["Hours_Studied", "Department"]]
y = df["Score"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)

# Scale numerical features
# StandardScaler transforms each column to have mean 0 and std dev 1
# (standardization), so no single feature dominates just because of its
# raw numeric range (e.g. Hours_Studied 2-10 vs Department 0-1).
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled features:")
print(X_scaled)

# --- Notes on fit_transform ---
# fit()       -> learns parameters from the data (e.g. mean/std, or category
#                mapping)
# transform() -> applies those learned parameters to actually change the data
# fit_transform() does both steps in one call. On new/unseen data (like a
# test set) you'd normally only call .transform(), reusing what was learned
# from the training data, so training and test data are scaled consistently.
