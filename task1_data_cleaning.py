import pandas as pd

print("=" * 60)
print("DATA CLEANING & STRUCTURAL VALIDATION")
print("=" * 60)

# Read dataset
df = pd.read_csv("raw_data.csv")

print("\nOriginal Dataset\n")
print(df)

print("\nDataset Information\n")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Email"] = df["Email"].fillna("not_available@email.com")
df["City"] = df["City"].replace(" ", "Unknown")
df["City"] = df["City"].fillna("Unknown")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())

# Standardize text
df["Name"] = df["Name"].str.title()
df["Email"] = df["Email"].str.lower()
df["City"] = df["City"].str.title()

# Convert date format
df["Join_Date"] = pd.to_datetime(
    df["Join_Date"],
    dayfirst=True,
    errors="coerce"
)

# Validate Age
median_age = df[(df["Age"] >= 0) & (df["Age"] <= 100)]["Age"].median()

df.loc[df["Age"] > 100, "Age"] = median_age

# Validate Purchase Amount
df.loc[df["Purchase_Amount"] < 0, "Purchase_Amount"] = 0

# Reset index
df = df.reset_index(drop=True)

print("\nCleaned Dataset\n")
print(df)

print("\nRemaining Missing Values")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Output File: cleaned_customer_data.csv")