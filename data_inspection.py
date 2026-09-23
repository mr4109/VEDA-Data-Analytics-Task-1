import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("data/Titanic-Dataset.csv")

# Display first 5 rows
print(df.head())

# Check dataset information
print("\n--- DATASET INFORMATION ---")
df.info()

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Number of duplicate rows:", df.duplicated().sum())

# Check unique values in categorical columns
print("\n--- UNIQUE VALUES ---")
print("Sex:", df["Sex"].unique())
print("Embarked:", df["Embarked"].unique())
print("Pclass:", df["Pclass"].unique())

# Statistical summary of numerical columns
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())