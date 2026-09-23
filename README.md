\# VEDA Technology - Data Analytics Task 1



\## Titanic Dataset — Data Cleaning and Preprocessing



This project was completed as part of the VEDA Technology Data Analytics Task 1.



The main objective of this project is to identify and fix common data quality issues in the Titanic dataset and prepare the data for reliable analysis.



\---



\## Objective



The project focuses on:



\- Identifying missing values

\- Checking duplicate records

\- Handling missing data appropriately

\- Standardizing data where required

\- Checking data types

\- Validating the cleaned dataset

\- Creating a change log documenting the cleaning process



\---



\## Tools Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Jupyter Notebook

\- Excel



\---



\## Dataset



The project uses the Titanic dataset.



Original dataset:



\- Rows: 891

\- Columns: 12



\---



\## Data Quality Issues Found



The initial inspection identified the following issues:



| Column | Issue | Count |

|---|---|---:|

| Age | Missing values | 177 |

| Cabin | Missing values | 687 |

| Embarked | Missing values | 2 |

| Entire rows | Duplicate rows | 0 |



\---



\## Data Cleaning Process



\### 1. Age



The `Age` column contained 177 missing values.



The missing values were replaced using the median age because the median is less affected by extreme values.



\### 2. Embarked



The `Embarked` column contained 2 missing values.



These values were replaced using the mode because `Embarked` is a categorical column.



\### 3. Cabin



The `Cabin` column contained 687 missing values.



Because a very large proportion of the column was missing, the `Cabin` column was removed from the cleaned dataset.



\### 4. Duplicate Rows



Duplicate rows were checked using Pandas.



No exact duplicate rows were found.



\---



\## Validation



After cleaning, the dataset was checked again.



Final results:



\- Rows: 891

\- Columns: 11

\- Missing values: 0

\- Duplicate rows: 0



\---



\## Project Structure



```text

VEDA-Data-Analytics-Task-1

│

├── .gitignore

├── README.md

├── requirements.txt

│

├── data

│   └── Titanic-Dataset.csv

│

├── notebook

│   └── Titanic\_Data\_Cleaning.ipynb

│

├── output

│   ├── Change-Log.xlsx

│   └── Titanic-Cleaned.csv

│

├── report

│

└── src

&#x20;   ├── data\_cleaning.py

&#x20;   └── data\_inspection.py

