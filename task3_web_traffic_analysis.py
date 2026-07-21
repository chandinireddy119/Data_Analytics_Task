import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("WEB TRAFFIC ANALYTICS")
print("=" * 60)

# Load Dataset
df = pd.read_csv("web_traffic.csv")

print("\nOriginal Dataset\n")
print(df)

print("\nDataset Information\n")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

df["Date"] = pd.to_datetime(df["Date"])

print("\nSummary Statistics")
print(df.describe())

print("\nTraffic Source Count")
print(df["TrafficSource"].value_counts())

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Visitors"], marker="o")
plt.title("Daily Website Visitors")
plt.xlabel("Date")
plt.ylabel("Visitors")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("web_traffic_analysis.png")
plt.show()

# Bar Chart
plt.figure(figsize=(6,5))
traffic = df["TrafficSource"].value_counts()
plt.bar(traffic.index, traffic.values)
plt.title("Traffic Source Analysis")
plt.xlabel("Traffic Source")
plt.ylabel("Number of Visits")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(traffic.values,
        labels=traffic.index,
        autopct="%1.1f%%")
plt.title("Traffic Source Distribution")
plt.show()

print("\nGraph saved as web_traffic_analysis.png")
print("\nTask 3 Completed Successfully!")