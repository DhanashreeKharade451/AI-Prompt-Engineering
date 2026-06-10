import pandas as pd

# Load dataset
df = pd.read_csv("../data/healthcare-ai-project/data/Test_Inpatientdata-1542969243754.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

#