import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 135, 180, 210, 195],
    "Customers": [30, 35, 32, 40, 48, 45]
}

df = pd.DataFrame(data)

print(df)

# Sales trend
df.plot(x="Month", y="Sales", kind="line", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Sales comparison
df.plot(x="Month", y="Sales", kind="bar")
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Sales vs Customers
df.plot(x="Customers", y="Sales", kind="scatter")
plt.title("Sales vs Customers")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.show()

# --- Answers from the output ---
highest_month = df.loc[df["Sales"].idxmax(), "Month"]
lowest_month = df.loc[df["Sales"].idxmin(), "Month"]

print(f"\nHighest sales month: {highest_month} ({df['Sales'].max()})")
print(f"Lowest sales month: {lowest_month} ({df['Sales'].min()})")

# Do sales generally increase over time?
# -> Mostly yes: Jan(120) -> Feb(150) -> Mar(135, dip) -> Apr(180) -> May(210) -> Jun(195, dip).
#    Overall upward trend with two small dips (Mar and Jun), not a perfectly straight increase.

# Does having more customers appear to be associated with higher sales?
# -> Yes. The scatter plot shows customers and sales rising together — months with more
#    customers (May: 48) tend to have higher sales (May: 210), and months with fewer
#    customers (Jan: 30) tend to have lower sales (Jan: 120). This suggests a positive
#    relationship, though it's not perfectly linear (e.g., Mar and Jun both dip slightly).
