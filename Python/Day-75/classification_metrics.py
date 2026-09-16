from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

actual = [1, 1, 0, 0, 1, 0, 1, 0]
predicted = [1, 0, 0, 0, 1, 1, 1, 0]

print("Accuracy:", accuracy_score(actual, predicted))
print("Precision:", precision_score(actual, predicted))
print("Recall:", recall_score(actual, predicted))
print("F1 Score:", f1_score(actual, predicted))

print("\nConfusion Matrix:")
print(confusion_matrix(actual, predicted))

# Reading the matrix (sklearn layout: rows = actual, cols = predicted,
# labels ordered [0, 1]):
#
#            Predicted 0   Predicted 1
# Actual 0       TN            FP
# Actual 1       FN            TP
#
# For this dataset the matrix comes out to:
#   [[3 1]
#    [1 3]]
#
# TN = 3  -> actual 0, predicted 0 (correctly caught the negatives)
# FP = 1  -> actual 0, predicted 1 (false alarm)
# FN = 1  -> actual 1, predicted 0 (missed a real positive)
# TP = 3  -> actual 1, predicted 1 (correctly caught the positives)
