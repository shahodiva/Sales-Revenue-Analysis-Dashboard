# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Part 6: KPI Dashboard
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os


# ------------------------------------------------------------
# 1. Load cleaned dataset
# ------------------------------------------------------------

file_path = "data/cleaned_sales_data.xlsx"

df = pd.read_excel(file_path)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Cleaned dataset loaded successfully!")


# ------------------------------------------------------------
# 2. Create dashboard output folder
# ------------------------------------------------------------

output_folder = "reports"

os.makedirs(output_folder, exist_ok=True)


# ------------------------------------------------------------
# 3. Calculate KPIs
# ------------------------------------------------------------

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_ID"].nunique()

total_products = df["Product_Name"].nunique()

total_quantity = df["Quantity"].sum()

average_order_value = total_sales / total_orders

profit_margin = (total_profit / total_sales) * 100


# ------------------------------------------------------------
# 4. Print KPIs
# ------------------------------------------------------------

print("\n========== DASHBOARD KPIs ==========")

print("Total Sales       : ₹", round(total_sales, 2))
print("Total Profit      : ₹", round(total_profit, 2))
print("Total Orders      :", total_orders)
print("Total Customers   :", total_customers)
print("Total Products    :", total_products)
print("Total Quantity    :", total_quantity)
print("Average Order     : ₹", round(average_order_value, 2))
print("Profit Margin     :", round(profit_margin, 2), "%")


# ------------------------------------------------------------
# 5. Prepare monthly sales
# ------------------------------------------------------------

monthly_sales = (
    df.set_index("Order_Date")["Sales"]
    .resample("ME")
    .sum()
)


# ------------------------------------------------------------
# 6. Prepare category sales
# ------------------------------------------------------------

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=True)
)


# ------------------------------------------------------------
# 7. Prepare regional sales
# ------------------------------------------------------------

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)


# ------------------------------------------------------------
# 8. Prepare top 10 products
# ------------------------------------------------------------

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=True)
    .tail(10)
)


# ------------------------------------------------------------
# 9. Create dashboard canvas
# ------------------------------------------------------------

fig = plt.figure(
    figsize=(18, 11)
)

fig.suptitle(
    "SALES & REVENUE ANALYSIS DASHBOARD",
    fontsize=22,
    fontweight="bold"
)


# ============================================================
# KPI CARDS
# ============================================================

kpi_data = [
    ("TOTAL SALES", f"₹{total_sales/10000000:.2f} Cr"),
    ("TOTAL PROFIT", f"₹{total_profit/10000000:.2f} Cr"),
    ("TOTAL ORDERS", f"{total_orders:,}"),
    ("CUSTOMERS", f"{total_customers:,}"),
    ("PRODUCTS", f"{total_products}"),
    ("AVG ORDER VALUE", f"₹{average_order_value:,.0f}"),
]


for i, (title, value) in enumerate(kpi_data):

    ax = fig.add_axes([
        0.04 + i * 0.158,
        0.78,
        0.145,
        0.12
    ])

    ax.axis("off")

    ax.text(
        0.5,
        0.65,
        title,
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

    ax.text(
        0.5,
        0.30,
        value,
        ha="center",
        va="center",
        fontsize=17,
        fontweight="bold"
    )


# ============================================================
# CHART 1 — MONTHLY SALES TREND
# ============================================================

ax1 = fig.add_axes([
    0.05,
    0.47,
    0.43,
    0.25
])

ax1.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

ax1.set_title(
    "Monthly Sales Trend",
    fontsize=13,
    fontweight="bold"
)

ax1.set_xlabel("Month")

ax1.set_ylabel("Sales")

ax1.tick_params(axis="x", rotation=45)


# ============================================================
# CHART 2 — SALES BY CATEGORY
# ============================================================

ax2 = fig.add_axes([
    0.54,
    0.47,
    0.41,
    0.25
])

ax2.bar(
    category_sales.index,
    category_sales.values
)

ax2.set_title(
    "Sales by Category",
    fontsize=13,
    fontweight="bold"
)

ax2.set_xlabel("Category")

ax2.set_ylabel("Sales")

ax2.tick_params(
    axis="x",
    rotation=30
)


# ============================================================
# CHART 3 — SALES BY REGION
# ============================================================

ax3 = fig.add_axes([
    0.05,
    0.10,
    0.40,
    0.25
])

ax3.bar(
    region_sales.index,
    region_sales.values
)

ax3.set_title(
    "Sales by Region",
    fontsize=13,
    fontweight="bold"
)

ax3.set_xlabel("Region")

ax3.set_ylabel("Sales")


# ============================================================
# CHART 4 — TOP 10 PRODUCTS
# ============================================================

ax4 = fig.add_axes([
    0.53,
    0.08,
    0.42,
    0.28
])

ax4.barh(
    top_products.index,
    top_products.values
)

ax4.set_title(
    "Top 10 Products by Sales",
    fontsize=13,
    fontweight="bold"
)

ax4.set_xlabel("Sales")


# ------------------------------------------------------------
# 10. Add dashboard footer
# ------------------------------------------------------------

fig.text(
    0.5,
    0.02,
    f"Profit Margin: {profit_margin:.2f}%  |  "
    f"Total Quantity Sold: {total_quantity:,}",
    ha="center",
    fontsize=11
)


# ------------------------------------------------------------
# 11. Save dashboard
# ------------------------------------------------------------

dashboard_file = (
    "reports/sales_revenue_dashboard.png"
)

plt.savefig(
    dashboard_file,
    dpi=300,
    bbox_inches="tight"
)


# ------------------------------------------------------------
# 12. Display dashboard
# ------------------------------------------------------------

plt.show()


# ------------------------------------------------------------
# 13. Completion message
# ------------------------------------------------------------

print("\n================================================")
print("KPI DASHBOARD CREATED SUCCESSFULLY")
print("================================================")

print("\nDashboard saved at:")

print(dashboard_file)