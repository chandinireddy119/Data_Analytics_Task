import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("CUSTOMER CHURN ANALYSIS")
print("=" * 60)

# Read dataset
df = pd.read_csv("customer_churn.csv")

print("\nOriginal Dataset\n")
print(df)

print("\nDataset Information\n")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Basic Statistics
total_customers = len(df)
churned = len(df[df["Churn"] == "Yes"])
retained = len(df[df["Churn"] == "No"])

print("\nTotal Customers:", total_customers)
print("Churned Customers:", churned)
print("Retained Customers:", retained)

churn_rate = (churned / total_customers) * 100
print("Churn Rate: {:.2f}%".format(churn_rate))

print("\nAverage Monthly Charges")
print(df.groupby("Churn")["MonthlyCharges"].mean())

print("\nAverage Login Frequency")
print(df.groupby("Churn")["LoginFrequency"].mean())

print("\nAverage Support Calls")
print(df.groupby("Churn")["SupportCalls"].mean())

# Bar Chart
counts = df["Churn"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(counts.index, counts.values)

plt.title("Customer Churn Analysis")
plt.xlabel("Churn Status")
plt.ylabel("Customers")

for i, value in enumerate(counts.values):
    plt.text(i, value + 0.1, str(value), ha="center")

plt.tight_layout()
plt.savefig("customer_churn_analysis.png")
plt.show()

print("\nGraph saved as customer_churn_analysis.png")
print("\nTask 2 Completed Successfully!")