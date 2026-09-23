import pandas as pd

# Load the original raw dataset
df = pd.read_csv("data/Titanic-Dataset.csv")

# Check missing values before cleaning
print("--- BEFORE CLEANING ---")
print(df.isnull().sum())

# Handle missing Age using median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Handle missing Embarked using mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove Cabin because most values are missing
df = df.drop(columns=["Cabin"])

# Check missing values after cleaning
print("\n--- AFTER CLEANING ---")
print(df.isnull().sum())

# Check duplicate rows after cleaning
print("\n--- DUPLICATE CHECK ---")
print("Duplicate rows:", df.duplicated().sum())

# Check data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# Check categorical values after cleaning
print("\n--- CATEGORICAL VALUES ---")
print("Sex:", df["Sex"].unique())
print("Embarked:", df["Embarked"].unique())
print("Pclass:", df["Pclass"].unique())

# Check numerical ranges
print("\n--- RANGE CHECK ---")
print("Age minimum:", df["Age"].min())
print("Age maximum:", df["Age"].max())
print("Fare minimum:", df["Fare"].min())
print("Fare maximum:", df["Fare"].max())

# Create change log
change_log = pd.DataFrame({
    "Issue": [
        "Missing Age",
        "Missing Embarked",
        "Missing Cabin",
        "Duplicate Rows"
    ],
    "Problem Found": [
        "177 missing values",
        "2 missing values",
        "687 missing values",
        "No duplicate rows found"
    ],
    "Action Taken": [
        "Filled missing values with median age",
        "Filled missing values with mode",
        "Removed Cabin column because most values were missing",
        "No action required"
    ],
    "Reason": [
        "Median is less affected by extreme values",
        "Embarked is categorical, so mode is suitable",
        "Around 77% values were missing, so imputation would not be reliable",
        "Dataset contained no exact duplicate rows"
    ]
})

print("\n--- CHANGE LOG ---")
print(change_log)

# Save cleaned dataset
df.to_csv("output/Titanic-Cleaned.csv", index=False)

# Save change log as Excel
change_log.to_excel("output/Change-Log.xlsx", index=False)

print("\nCleaned dataset and change log saved successfully.")