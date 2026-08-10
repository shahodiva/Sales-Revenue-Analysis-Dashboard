# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Part 2: Data Loading and Dataset Inspection
# ============================================================

import pandas as pd
import os

# ------------------------------------------------------------
# 1. Define the dataset path
# ------------------------------------------------------------

file_path = "data/sales_data.xlsx"

# ------------------------------------------------------------
# 2. Check whether the file exists
# ------------------------------------------------------------

if os.path.exists(file_path):
    print("Dataset found successfully!")
else:
    print("Dataset not found!")
    print("Check the file path:", file_path)


# ------------------------------------------------------------
# 3. Load the Excel dataset
# ------------------------------------------------------------

df = pd.read_excel(file_path)


# ------------------------------------------------------------
# 4. Display the first 10 records
# ------------------------------------------------------------

print("\n========== FIRST 10 RECORDS ==========\n")
print(df.head(10))


# ------------------------------------------------------------
# 5. Display the last 5 records
# ------------------------------------------------------------

print("\n========== LAST 5 RECORDS ==========\n")
print(df.tail())


# ------------------------------------------------------------
# 6. Display number of rows and columns
# ------------------------------------------------------------

print("\n========== DATASET SHAPE ==========\n")
print("Number of Rows    :", df.shape[0])
print("Number of Columns :", df.shape[1])


# ------------------------------------------------------------
# 7. Display column names
# ------------------------------------------------------------

print("\n========== COLUMN NAMES ==========\n")

for column in df.columns:
    print(column)


# ------------------------------------------------------------
# 8. Display data types
# ------------------------------------------------------------

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)


# ------------------------------------------------------------
# 9. Display dataset information
# ------------------------------------------------------------

print("\n========== DATASET INFORMATION ==========\n")
df.info()


# ------------------------------------------------------------
# 10. Display statistical summary
# ------------------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())


# ------------------------------------------------------------
# 11. Count unique values
# ------------------------------------------------------------

print("\n========== UNIQUE VALUES ==========\n")

print("Unique Orders      :", df["Order_ID"].nunique())
print("Unique Customers   :", df["Customer_ID"].nunique())
print("Unique Products    :", df["Product_Name"].nunique())
print("Unique Categories  :", df["Category"].nunique())
print("Unique Regions     :", df["Region"].nunique())


# ------------------------------------------------------------
# 12. Display category values
# ------------------------------------------------------------

print("\n========== PRODUCT CATEGORIES ==========\n")
print(df["Category"].unique())


# ------------------------------------------------------------
# 13. Display regions
# ------------------------------------------------------------

print("\n========== REGIONS ==========\n")
print(df["Region"].unique())


# ------------------------------------------------------------
# 14. Display payment methods
# ------------------------------------------------------------

print("\n========== PAYMENT METHODS ==========\n")
print(df["Payment_Method"].unique())


# ------------------------------------------------------------
# 15. Display date range
# ------------------------------------------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n========== DATE RANGE ==========\n")
print("Starting Date :", df["Order_Date"].min())
print("Ending Date   :", df["Order_Date"].max())


# ------------------------------------------------------------
# 16. Display basic sales information
# ------------------------------------------------------------

print("\n========== SALES SUMMARY ==========\n")

print("Total Sales   : ₹", round(df["Sales"].sum(), 2))
print("Total Cost    : ₹", round(df["Cost"].sum(), 2))
print("Total Profit  : ₹", round(df["Profit"].sum(), 2))
print("Total Quantity:", df["Quantity"].sum())


# ------------------------------------------------------------
# 17. Display first five rows in table format
# ------------------------------------------------------------

print("\n========== DATASET PREVIEW ==========\n")
print(df.head().to_string(index=False))


print("\n================================================")
print("DATA LOADING AND INSPECTION COMPLETED")
print("================================================")