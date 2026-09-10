# Day 70 — Data Preprocessing for ML

## Pipeline
```
Raw Data
   ↓
Clean Data
   ↓
Select Features
   ↓
Encode Categorical Data
   ↓
Scale Numerical Data
   ↓
Training-ready Data
```

Preprocessing converts raw data into a form suitable for machine-learning algorithms.

## Concepts

**Feature**
An input column used by the model to make predictions. In `Hours_Studied, Attendance, Sleep → Exam_Score`, the first three columns are features.

**Target**
The value the model is trying to predict (the output). In the example above, `Exam_Score` is the target. Conventionally called `X` (features) and `y` (target).

**Categorical data**
Data that represents categories/labels rather than numbers, e.g. `Department: AI, CSE, ECE`. Most ML algorithms work with numbers, so categorical columns must be converted before training.

**Encoding**
The process of converting categorical values into numbers. Simplest form is label encoding, mapping each unique category to an integer:
```
AI  → 0
CSE → 1
ECE → 2
```

**Feature scaling**
Transforming numeric feature values so they're on comparable ranges/scales. Needed because raw features can have very different ranges (e.g. `Hours_Studied` from 0-10 vs. `Salary` from 0-100000), and some algorithms (distance-based ones like KNN, gradient-descent-based ones) are sensitive to that difference — a large-range feature can dominate just because of its scale, not because it's more important.

**Normalization**
Rescales values into a fixed range, typically [0, 1], based on the min and max of the data.

**Standardization**
Rescales values so they have mean 0 and standard deviation 1 — i.e. expresses each value as "how many standard deviations from the mean." Doesn't bound values to a fixed range like normalization does.

**LabelEncoder**
A scikit-learn tool that performs label encoding — turns a column of category strings into integer codes (alphabetical order by default).

**StandardScaler**
A scikit-learn tool that performs standardization — transforms a numeric column to mean 0, std dev 1.

## Key methods
- `fit()` — learns parameters from the data (e.g. mean/std for a scaler, category mapping for an encoder).
- `transform()` — applies the learned parameters to actually transform the data.
- `fit_transform()` — does both in one call, used on training data. On new/unseen data you'd typically only call `.transform()` so it's scaled/encoded consistently with what was learned on training data.
