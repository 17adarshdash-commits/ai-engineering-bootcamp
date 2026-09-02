# Day 62 — NumPy Foundations

## 1. What is NumPy?

NumPy (Numerical Python) is a library that provides fast, efficient data
structures and operations for numerical data — mainly the **array**.
Regular Python lists are general-purpose and flexible, but slow for
math-heavy work because they're built to hold any type of object. NumPy
arrays store data in a compact, uniform block of memory and let NumPy run
operations in optimized, low-level code instead of a Python loop. This is
why almost every ML/data science library (pandas, scikit-learn, PyTorch,
TensorFlow) is built on top of NumPy arrays.

## 2. NumPy array

A NumPy array (`ndarray`) is a grid of values, all of the **same data
type**, indexed by a tuple of non-negative integers. Created with
`np.array([...])`.

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
```

## 3. shape

`arr.shape` tells you the size of the array along each dimension, as a
tuple.

- `[1, 2, 3, 4, 5]` → shape `(5,)` — 5 elements in one dimension.
- `[[1, 2, 3], [4, 5, 6]]` → shape `(2, 3)` — 2 rows, 3 columns.

## 4. ndim

`arr.ndim` tells you how many dimensions (axes) the array has.

- A 1D array (a flat list of numbers) → `ndim = 1`
- A 2D array (a list of lists / matrix) → `ndim = 2`

## 5. dtype

`arr.dtype` tells you the data type of the elements stored in the array
(e.g. `int64`, `float64`). Unlike a Python list, every element in a NumPy
array must share the same dtype — that uniformity is part of what makes
NumPy fast.

## 6. 1D array

A single row of values, like a plain list:

```
[1, 2, 3]
```

## 7. 2D array

A list of lists — rows and columns, like a matrix:

```
[
 [1, 2, 3],
 [4, 5, 6]
]
```

## 8. Vectorized operations

Vectorized operations let you apply math to an entire array at once,
without writing an explicit Python `for` loop:

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

a + b   # element-wise addition
a - b   # element-wise subtraction
a * b   # element-wise multiplication
a / b   # element-wise division
```

NumPy also provides aggregate functions like `np.sum(a)`, `np.mean(a)`,
`np.max(a)`, and `np.min(a)` that reduce a whole array down to one number.
Vectorization is both more concise and much faster than looping in plain
Python.

## Big picture

```
Python List
     ↓
General-purpose collection

NumPy Array
     ↓
Numerical computation
     ↓
ML / Data Science / Scientific Computing
```
