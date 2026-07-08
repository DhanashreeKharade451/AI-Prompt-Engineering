import pandas as pd

# Load dataset
df = pd.read_csv("../data/Test_Inpatientdata-1542969243754.csv")

# View data
print(df.head())
print(df.info())
print(df.describe())

# Missing values before cleaning
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
print("after Dropping duplicate records")
print(df.drop_duplicates(inplace=True))

# Create features:
df["claim_per_day"] = df["ClaimAmount"] / df["DaysAdmitted"]
