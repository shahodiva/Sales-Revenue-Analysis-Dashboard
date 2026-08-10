# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Part 3: Data Cleaning and Preprocessing
# ============================================================

import pandas as pd
import os


# ------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------

file_path = "data/sales_data.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")


# ------------------------------------------------------------
# 2. Display original dataset size
# ------------------------------------------------------------

print("\n========== ORIGINAL DATASET ==========")

print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ------------------------------------------------------------
# 3. Check missing values
# ------------------------------------------------------------

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

total_missing = missing_values.sum()

print("\nTotal Missing Values:", total_missing)


# ------------------------------------------------------------
# 4. Check duplicate records
# ------------------------------------------------------------

print("\n========== DUPLICATE RECORDS ==========")

duplicate_count = df.duplicated().sum()

print("Duplicate Records:", duplicate_count)


# ------------------------------------------------------------
# 5. Remove duplicate records
# ------------------------------------------------------------

if duplicate_count > 0:

    df = df.drop_duplicates()

    print("Duplicate records removed.")

else:

    print("No duplicate records found.")


# ------------------------------------------------------------
# 6. Convert Order_Date to datetime
# ------------------------------------------------------------

print("\n========== DATE CONVERSION ==========")

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("Order_Date converted to datetime.")


# ------------------------------------------------------------
# 7. Check invalid dates
# ------------------------------------------------------------

invalid_dates = df["Order_Date"].isnull().sum()

print("Invalid Dates:", invalid_dates)


# ------------------------------------------------------------
# 8. Check numeric columns
# ------------------------------------------------------------

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

print("\n========== NUMERIC COLUMN CHECK ==========")

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    print(column, ":", df[column].dtype)


# ------------------------------------------------------------
# 9. Check invalid quantity values
# ------------------------------------------------------------

print("\n========== QUANTITY VALIDATION ==========")

invalid_quantity = (df["Quantity"] <= 0).sum()

print("Invalid Quantity Records:", invalid_quantity)


# ------------------------------------------------------------
# 10. Check invalid prices
# ------------------------------------------------------------

print("\n========== PRICE VALIDATION ==========")

invalid_price = (df["Unit_Price"] <= 0).sum()

print("Invalid Unit Price Records:", invalid_price)


# ------------------------------------------------------------
# 11. Check invalid sales values
# ------------------------------------------------------------

print("\n========== SALES VALIDATION ==========")

invalid_sales = (df["Sales"] <= 0).sum()

print("Invalid Sales Records:", invalid_sales)


# ------------------------------------------------------------
# 12. Check invalid cost values
# ------------------------------------------------------------

print("\n========== COST VALIDATION ==========")

invalid_cost = (df["Cost"] <= 0).sum()

print("Invalid Cost Records:", invalid_cost)


# ------------------------------------------------------------
# 13. Check invalid profit values
# ------------------------------------------------------------

print("\n========== PROFIT VALIDATION ==========")

invalid_profit = (df["Profit"] < 0).sum()

print("Negative Profit Records:", invalid_profit)


# ------------------------------------------------------------
# 14. Check discount range
# ------------------------------------------------------------

print("\n========== DISCOUNT VALIDATION ==========")

invalid_discount = (
    (df["Discount"] < 0) |
    (df["Discount"] > 1)
).sum()

print("Invalid Discount Records:", invalid_discount)


# ------------------------------------------------------------
# 15. Remove invalid records
# ------------------------------------------------------------

df = df[
    (df["Quantity"] > 0) &
    (df["Unit_Price"] > 0) &
    (df["Sales"] > 0) &
    (df["Cost"] > 0) &
    (df["Discount"] >= 0) &
    (df["Discount"] <= 1)
]


# ------------------------------------------------------------
# 16. Create additional date columns
# ------------------------------------------------------------

df["Year"] = df["Order_Date"].dt.year

df["Month"] = df["Order_Date"].dt.month

df["Month_Name"] = df["Order_Date"].dt.strftime("%B")

df["Quarter"] = (
    "Q" + df["Order_Date"].dt.quarter.astype(str)
)


# ------------------------------------------------------------
# 17. Calculate Profit Margin
# ------------------------------------------------------------

df["Profit_Margin"] = (
    df["Profit"] / df["Sales"]
) * 100


# ------------------------------------------------------------
# 18. Calculate Average Order Value
# ------------------------------------------------------------

total_sales = df["Sales"].sum()

total_orders = df["Order_ID"].nunique()

average_order_value = total_sales / total_orders

print("\n========== AVERAGE ORDER VALUE ==========")

print(
    "Average Order Value: ₹",
    round(average_order_value, 2)
)


# ------------------------------------------------------------
# 19. Final dataset information
# ------------------------------------------------------------

print("\n========== CLEANED DATASET ==========")

print("Rows    :", df.shape[0])

print("Columns :", df.shape[1])


# ------------------------------------------------------------
# 20. Check final missing values
# ------------------------------------------------------------

print("\n========== FINAL MISSING VALUES ==========")

print(df.isnull().sum().sum())


# ------------------------------------------------------------
# 21. Display cleaned dataset
# ------------------------------------------------------------

print("\n========== CLEANED DATA PREVIEW ==========")

print(
    df.head().to_string(index=False)
)


# ------------------------------------------------------------
# 22. Create cleaned-data folder
# ------------------------------------------------------------

output_folder = "data"

if not os.path.exists(output_folder):

    os.makedirs(output_folder)


# ------------------------------------------------------------
# 23. Save cleaned dataset
# ------------------------------------------------------------

output_file = "data/cleaned_sales_data.xlsx"

df.to_excel(
    output_file,
    index=False
)


# ------------------------------------------------------------
# 24. Save CSV version
# ------------------------------------------------------------

csv_file = "data/cleaned_sales_data.csv"

df.to_csv(
    csv_file,
    index=False
)


# ------------------------------------------------------------
# 25. Final message
# ------------------------------------------------------------

print("\n================================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("================================================")

print("\nCleaned Excel file:")
print(output_file)

print("\nCleaned CSV file:")
print(csv_file)