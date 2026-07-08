#machine Learning
# *****************

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("../data/Test_Inpatientdata-1542969243754.csv")

# Target column
# Fraud = 1, Not Fraud = 0

print(df.head())

X = df.drop("Fraud", axis=1)
y = df["Fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()

# Train
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print(classification_report(y_test, y_pred))