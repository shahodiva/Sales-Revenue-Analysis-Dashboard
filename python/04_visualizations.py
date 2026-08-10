# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Part 5: Data Visualizations
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ------------------------------------------------------------
# 1. Load cleaned dataset
# ------------------------------------------------------------

file_path = "data/cleaned_sales_data.xlsx"

df = pd.read_excel(file_path)

print("Cleaned dataset loaded successfully!")


# ------------------------------------------------------------
# 2. Create visualization folder
# ------------------------------------------------------------

output_folder = "reports/charts"

os.makedirs(output_folder, exist_ok=True)


# ------------------------------------------------------------
# 3. Convert date column
# ------------------------------------------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# ============================================================
# CHART 1 — MONTHLY SALES TREND
# ============================================================

monthly_sales = (
    df.groupby("Order_Date")["Sales"]
    .sum()
    .resample("ME")
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/01_monthly_sales_trend.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 2 — MONTHLY PROFIT TREND
# ============================================================

monthly_profit = (
    df.groupby("Order_Date")["Profit"]
    .sum()
    .resample("ME")
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_profit.index,
    monthly_profit.values,
    marker="o"
)

plt.title("Monthly Profit Trend")

plt.xlabel("Month")

plt.ylabel("Profit")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/02_monthly_profit_trend.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 3 — SALES BY CATEGORY
# ============================================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_sales.plot(
    kind="bar"
)

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/03_sales_by_category.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 4 — PROFIT BY CATEGORY
# ============================================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_profit.plot(
    kind="bar"
)

plt.title("Profit by Category")

plt.xlabel("Category")

plt.ylabel("Profit")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/04_profit_by_category.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 5 — SALES BY REGION
# ============================================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

region_sales.plot(
    kind="bar"
)

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/05_sales_by_region.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 6 — TOP 10 PRODUCTS
# ============================================================

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 7))

top_products.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Products by Sales")

plt.xlabel("Sales")

plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/06_top_10_products.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 7 — SALES BY PAYMENT METHOD
# ============================================================

payment_sales = (
    df.groupby("Payment_Method")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

payment_sales.plot(
    kind="bar"
)

plt.title("Sales by Payment Method")

plt.xlabel("Payment Method")

plt.ylabel("Sales")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/07_sales_by_payment_method.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 8 — SALES DISTRIBUTION BY CATEGORY
# ============================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Category",
    y="Sales"
)

plt.title("Sales Distribution by Category")

plt.xlabel("Category")

plt.ylabel("Sales")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/08_sales_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 9 — SALES VS PROFIT
# ============================================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)

plt.title("Sales vs Profit")

plt.xlabel("Sales")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/09_sales_vs_profit.png",
    dpi=300
)

plt.show()


# ============================================================
# CHART 10 — QUANTITY BY CATEGORY
# ============================================================

category_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_quantity.plot(
    kind="bar"
)

plt.title("Quantity Sold by Category")

plt.xlabel("Category")

plt.ylabel("Quantity")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/10_quantity_by_category.png",
    dpi=300
)

plt.show()


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n================================================")
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY")
print("================================================")

print("\nCharts saved in:")

print(output_folder)