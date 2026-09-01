# Day 61 - ML Basics: understanding how ML data is represented
# No scikit-learn yet — just plain Python.

hours = [1, 2, 3, 4, 5]
scores = [45, 50, 60, 68, 75]

num_students = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / num_students

print("Number of students:", num_students)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Average score:", average_score)

print()

emails = [
    ("Win a free prize", "spam"),
    ("Meeting at 5pm", "not spam"),
    ("You won money", "spam"),
    ("Submit assignment tomorrow", "not spam"),
]

for email_text, label in emails:
    print(f"Email: {email_text!r} -> Label: {label}")
