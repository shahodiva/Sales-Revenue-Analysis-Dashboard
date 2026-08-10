# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Part 4: Exploratory Sales Analysis
# ============================================================

import pandas as pd


# ------------------------------------------------------------
# 1. Load cleaned dataset
# ------------------------------------------------------------

file_path = "data/cleaned_sales_data.xlsx"

df = pd.read_excel(file_path)

print("Cleaned dataset loaded successfully!")


# ------------------------------------------------------------
# 2. Basic KPI Analysis
# ------------------------------------------------------------

total_sales = df["Sales"].sum()
total_cost = df["Cost"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
total_products = df["Product_Name"].nunique()


print("\n========== KEY PERFORMANCE INDICATORS ==========")

print("Total Sales       : ₹", round(total_sales, 2))
print("Total Cost        : ₹", round(total_cost, 2))
print("Total Profit      : ₹", round(total_profit, 2))
print("Total Quantity    :", total_quantity)
print("Total Orders      :", total_orders)
print("Total Customers   :", total_customers)
print("Total Products    :", total_products)


# ------------------------------------------------------------
# 3. Overall Profit Margin
# ------------------------------------------------------------

profit_margin = (
    total_profit / total_sales
) * 100

print("\nOverall Profit Margin:",
      round(profit_margin, 2), "%")


# ------------------------------------------------------------
# 4. Sales by Category
# ------------------------------------------------------------

print("\n========== SALES BY CATEGORY ==========")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)


# ------------------------------------------------------------
# 5. Profit by Category
# ------------------------------------------------------------

print("\n========== PROFIT BY CATEGORY ==========")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)


# ------------------------------------------------------------
# 6. Quantity by Category
# ------------------------------------------------------------

print("\n========== QUANTITY BY CATEGORY ==========")

category_quantity = (
    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(category_quantity)


# ------------------------------------------------------------
# 7. Sales by Region
# ------------------------------------------------------------

print("\n========== SALES BY REGION ==========")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(region_sales)


# ------------------------------------------------------------
# 8. Profit by Region
# ------------------------------------------------------------

print("\n========== PROFIT BY REGION ==========")

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)


# ------------------------------------------------------------
# 9. Monthly Sales
# ------------------------------------------------------------

print("\n========== MONTHLY SALES ==========")

monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

print(monthly_sales)


# ------------------------------------------------------------
# 10. Yearly Sales
# ------------------------------------------------------------

print("\n========== YEARLY SALES ==========")

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

print(yearly_sales)


# ------------------------------------------------------------
# 11. Top 10 Products by Sales
# ------------------------------------------------------------

print("\n========== TOP 10 PRODUCTS BY SALES ==========")

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)


# ------------------------------------------------------------
# 12. Top 10 Products by Profit
# ------------------------------------------------------------

print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")

top_profit_products = (
    df.groupby("Product_Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_profit_products)


# ------------------------------------------------------------
# 13. Sales by Payment Method
# ------------------------------------------------------------

print("\n========== SALES BY PAYMENT METHOD ==========")

payment_sales = (
    df.groupby("Payment_Method")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_sales)


# ------------------------------------------------------------
# 14. Orders by Payment Method
# ------------------------------------------------------------

print("\n========== ORDERS BY PAYMENT METHOD ==========")

payment_orders = (
    df.groupby("Payment_Method")["Order_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print(payment_orders)


# ------------------------------------------------------------
# 15. Top 10 States by Sales
# ------------------------------------------------------------

print("\n========== TOP 10 STATES BY SALES ==========")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_states)


# ------------------------------------------------------------
# 16. Top 10 Customers by Sales
# ------------------------------------------------------------

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

top_customers = (
    df.groupby("Customer_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)


# ------------------------------------------------------------
# 17. Average Order Value
# ------------------------------------------------------------

average_order_value = (
    total_sales / total_orders
)

print("\n========== AVERAGE ORDER VALUE ==========")

print(
    "Average Order Value : ₹",
    round(average_order_value, 2)
)


# ------------------------------------------------------------
# 18. Average Profit per Order
# ------------------------------------------------------------

average_profit_order = (
    total_profit / total_orders
)

print(
    "Average Profit per Order : ₹",
    round(average_profit_order, 2)
)


# ------------------------------------------------------------
# 19. Best Category
# ------------------------------------------------------------

best_category = category_sales.idxmax()

print("\n========== BEST PERFORMING CATEGORY ==========")

print("Best Category:", best_category)

print(
    "Sales: ₹",
    round(category_sales.max(), 2)
)


# ------------------------------------------------------------
# 20. Best Region
# ------------------------------------------------------------

best_region = region_sales.idxmax()

print("\n========== BEST PERFORMING REGION ==========")

print("Best Region:", best_region)

print(
    "Sales: ₹",
    round(region_sales.max(), 2)
)


# ------------------------------------------------------------
# 21. Best Product
# ------------------------------------------------------------

best_product = top_products.idxmax()

print("\n========== BEST PERFORMING PRODUCT ==========")

print("Best Product:", best_product)

print(
    "Sales: ₹",
    round(top_products.max(), 2)
)


# ------------------------------------------------------------
# 22. Final Message
# ------------------------------------------------------------

print("\n================================================")
print("SALES ANALYSIS COMPLETED SUCCESSFULLY")
print("================================================")