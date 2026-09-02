# Day 62 - NumPy Basics: arrays, shape, ndim, dtype, and vectorized operations

import numpy as np

# Step 1 & 2 — create marks array and inspect it
marks = np.array([72, 85, 91, 64, 78])

print("Marks:", marks)
print("Number of students:", marks.size)
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))
print("Average mark:", np.mean(marks))
print("Shape:", marks.shape)
print("Number of dimensions:", marks.ndim)
print("Data type:", marks.dtype)

print()

# Step 3 — add bonus marks using vectorized addition
bonus = np.array([3, 2, 1, 4, 2])
updated_marks = marks + bonus

print("Updated marks:", updated_marks)

print()

# Step 4 — a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Matrix:\n", matrix)
print("Matrix shape:", matrix.shape)
print("Matrix ndim:", matrix.ndim)
