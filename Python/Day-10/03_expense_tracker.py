expenses = []
for i in range(5):
    expense = float(input("Add expense: "))
    expenses.append(expense)

print(f"Total expenditure: {sum(expenses)} rupees")
print(f"Average expense: {sum(expenses) / 5} rupees")
print(f"Highest expense: {max(expenses)} rupees")
print(f"Lowest expense: {min(expenses)} rupees")