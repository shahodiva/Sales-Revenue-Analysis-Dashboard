# ============================================================
# SALES & REVENUE ANALYSIS DASHBOARD
# Interactive Business Intelligence Dashboard
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .dashboard-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .dashboard-subtitle {
        text-align: center;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    file_path = "data/cleaned_sales_data.xlsx"

    data = pd.read_excel(file_path)

    data["Order_Date"] = pd.to_datetime(
        data["Order_Date"]
    )

    return data


df = load_data()


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="dashboard-title">'
    '📊 Sales & Revenue Analysis Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Business Intelligence & Performance Analysis'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Dashboard Filters")

st.sidebar.markdown(
    "Use the filters below to analyze specific parts of the business."
)


# ============================================================
# RESET BUTTON
# ============================================================

if st.sidebar.button(
    "🔄 Reset Filters",
    width="stretch"
):

    st.rerun()


# ============================================================
# YEAR FILTER
# ============================================================

years = sorted(
    df["Year"].dropna().unique()
)

selected_year = st.sidebar.multiselect(
    "📅 Select Year",
    options=years,
    default=years
)


# ============================================================
# REGION FILTER
# ============================================================

regions = sorted(
    df["Region"].dropna().unique()
)

selected_region = st.sidebar.multiselect(
    "🌎 Select Region",
    options=regions,
    default=regions
)


# ============================================================
# CATEGORY FILTER
# ============================================================

categories = sorted(
    df["Category"].dropna().unique()
)

selected_category = st.sidebar.multiselect(
    "🏷️ Select Category",
    options=categories,
    default=categories
)


# ============================================================
# PAYMENT METHOD FILTER
# ============================================================

payment_methods = sorted(
    df["Payment_Method"].dropna().unique()
)

selected_payment = st.sidebar.multiselect(
    "💳 Select Payment Method",
    options=payment_methods,
    default=payment_methods
)


# ============================================================
# DATE RANGE FILTER
# ============================================================

st.sidebar.subheader("📅 Date Range")

min_date = df["Order_Date"].min().date()

max_date = df["Order_Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# ============================================================
# APPLY FILTERS
# ============================================================

if len(selected_dates) == 2:

    start_date = pd.Timestamp(
        selected_dates[0]
    )

    end_date = pd.Timestamp(
        selected_dates[1]
    )

    filtered_df = df[
        (df["Year"].isin(selected_year)) &
        (df["Region"].isin(selected_region)) &
        (df["Category"].isin(selected_category)) &
        (df["Payment_Method"].isin(selected_payment)) &
        (df["Order_Date"] >= start_date) &
        (df["Order_Date"] <= end_date)
    ].copy()

else:

    filtered_df = df[
        (df["Year"].isin(selected_year)) &
        (df["Region"].isin(selected_region)) &
        (df["Category"].isin(selected_category)) &
        (df["Payment_Method"].isin(selected_payment))
    ].copy()


# ============================================================
# CHECK FILTERED DATA
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No data available for the selected filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_cost = filtered_df["Cost"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_products = filtered_df["Product_Name"].nunique()

total_quantity = filtered_df["Quantity"].sum()

average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

profit_margin = (
    total_profit / total_sales * 100
    if total_sales > 0
    else 0
)


# ============================================================
# KPI SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📌 Key Performance Indicators</div>',
    unsafe_allow_html=True
)


# First row

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "💰 Total Sales",
        f"₹{total_sales:,.2f}"
    )


with col2:

    st.metric(
        "📈 Total Profit",
        f"₹{total_profit:,.2f}"
    )


with col3:

    st.metric(
        "🛒 Total Orders",
        f"{total_orders:,}"
    )


with col4:

    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )


# Second row

col5, col6, col7, col8 = st.columns(4)


with col5:

    st.metric(
        "📦 Products",
        f"{total_products:,}"
    )


with col6:

    st.metric(
        "🔢 Quantity Sold",
        f"{total_quantity:,}"
    )


with col7:

    st.metric(
        "🧾 Average Order Value",
        f"₹{average_order_value:,.2f}"
    )


with col8:

    st.metric(
        "📊 Profit Margin",
        f"{profit_margin:.2f}%"
    )


st.divider()


# ============================================================
# MONTHLY SALES TREND
# ============================================================

st.markdown(
    '<div class="section-title">📈 Revenue Trend</div>',
    unsafe_allow_html=True
)


monthly_sales = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order_Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)


fig_monthly_sales = px.line(
    monthly_sales,
    x="Order_Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)


fig_monthly_sales.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales",
    hovermode="x unified"
)


st.plotly_chart(
    fig_monthly_sales,
    width="stretch"
)


# ============================================================
# MONTHLY PROFIT TREND
# ============================================================

monthly_profit = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order_Date",
            freq="ME"
        )
    )["Profit"]
    .sum()
    .reset_index()
)


fig_monthly_profit = px.line(
    monthly_profit,
    x="Order_Date",
    y="Profit",
    markers=True,
    title="Monthly Profit Trend"
)


fig_monthly_profit.update_layout(
    xaxis_title="Month",
    yaxis_title="Profit",
    hovermode="x unified"
)


st.plotly_chart(
    fig_monthly_profit,
    width="stretch"
)


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">🏷️ Category Analysis</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ------------------------------------------------------------
# Sales by Category
# ------------------------------------------------------------

with col1:

    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_category_sales = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=".2s"
    )

    fig_category_sales.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_category_sales,
        width="stretch"
    )


# ------------------------------------------------------------
# Profit by Category
# ------------------------------------------------------------

with col2:

    category_profit = (
        filtered_df
        .groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values(
            "Profit",
            ascending=False
        )
    )

    fig_category_profit = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category",
        text_auto=".2s"
    )

    fig_category_profit.update_layout(
        xaxis_title="Category",
        yaxis_title="Profit"
    )

    st.plotly_chart(
        fig_category_profit,
        width="stretch"
    )


# ============================================================
# REGIONAL ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">🌎 Regional Analysis</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ------------------------------------------------------------
# Sales by Region
# ------------------------------------------------------------

with col1:

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=".2s"
    )

    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_region,
        width="stretch"
    )


# ------------------------------------------------------------
# Profit by Region
# ------------------------------------------------------------

with col2:

    region_profit = (
        filtered_df
        .groupby("Region")["Profit"]
        .sum()
        .reset_index()
        .sort_values(
            "Profit",
            ascending=False
        )
    )

    fig_region_profit = px.bar(
        region_profit,
        x="Region",
        y="Profit",
        title="Profit by Region",
        text_auto=".2s"
    )

    fig_region_profit.update_layout(
        xaxis_title="Region",
        yaxis_title="Profit"
    )

    st.plotly_chart(
        fig_region_profit,
        width="stretch"
    )


# ============================================================
# TOP 10 PRODUCTS
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Product Performance</div>',
    unsafe_allow_html=True
)


top_products = (
    filtered_df
    .groupby("Product_Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)


fig_products = px.bar(
    top_products.sort_values("Sales"),
    x="Sales",
    y="Product_Name",
    orientation="h",
    title="Top 10 Products by Sales",
    text_auto=".2s"
)


fig_products.update_layout(
    xaxis_title="Sales",
    yaxis_title="Product"
)


st.plotly_chart(
    fig_products,
    width="stretch"
)


# ============================================================
# PAYMENT METHOD ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">💳 Payment Analysis</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ------------------------------------------------------------
# Payment Sales
# ------------------------------------------------------------

with col1:

    payment_sales = (
        filtered_df
        .groupby("Payment_Method")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig_payment_bar = px.bar(
        payment_sales,
        x="Payment_Method",
        y="Sales",
        title="Sales by Payment Method",
        text_auto=".2s"
    )

    fig_payment_bar.update_layout(
        xaxis_title="Payment Method",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_payment_bar,
        width="stretch"
    )


# ------------------------------------------------------------
# Payment Distribution
# ------------------------------------------------------------

with col2:

    fig_payment_pie = px.pie(
        payment_sales,
        names="Payment_Method",
        values="Sales",
        title="Revenue Distribution by Payment Method"
    )

    st.plotly_chart(
        fig_payment_pie,
        width="stretch"
    )


# ============================================================
# SALES VS PROFIT
# ============================================================

st.markdown(
    '<div class="section-title">📊 Sales vs Profit Analysis</div>',
    unsafe_allow_html=True
)


fig_scatter = px.scatter(
    filtered_df,
    x="Sales",
    y="Profit",
    color="Category",
    size="Quantity",
    hover_data=[
        "Product_Name",
        "Region",
        "Customer_Name",
        "Payment_Method"
    ],
    title="Sales vs Profit"
)


fig_scatter.update_layout(
    xaxis_title="Sales",
    yaxis_title="Profit"
)


st.plotly_chart(
    fig_scatter,
    width="stretch"
)


# ============================================================
# TOP 10 CUSTOMERS
# ============================================================

st.markdown(
    '<div class="section-title">👑 Customer Performance</div>',
    unsafe_allow_html=True
)


top_customers = (
    filtered_df
    .groupby("Customer_Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)


fig_customers = px.bar(
    top_customers.sort_values("Sales"),
    x="Sales",
    y="Customer_Name",
    orientation="h",
    title="Top 10 Customers by Revenue",
    text_auto=".2s"
)


fig_customers.update_layout(
    xaxis_title="Sales",
    yaxis_title="Customer"
)


st.plotly_chart(
    fig_customers,
    width="stretch"
)


# ============================================================
# ADVANCED BUSINESS INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 Advanced Business Insights</div>',
    unsafe_allow_html=True
)


# ============================================================
# MONTHLY PERFORMANCE
# ============================================================

monthly_analysis = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order_Date",
            freq="ME"
        )
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
)


if not monthly_analysis.empty:

    best_month_row = monthly_analysis.loc[
        monthly_analysis["Sales"].idxmax()
    ]

    lowest_month_row = monthly_analysis.loc[
        monthly_analysis["Sales"].idxmin()
    ]

    best_month = best_month_row["Order_Date"].strftime(
        "%B %Y"
    )

    lowest_month = lowest_month_row["Order_Date"].strftime(
        "%B %Y"
    )

    best_month_sales = best_month_row["Sales"]

    lowest_month_sales = lowest_month_row["Sales"]

else:

    best_month = "N/A"
    lowest_month = "N/A"

    best_month_sales = 0
    lowest_month_sales = 0


# ============================================================
# PRODUCT PERFORMANCE
# ============================================================

product_analysis = (
    filtered_df
    .groupby("Product_Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)


if not product_analysis.empty:

    best_selling_product = product_analysis.loc[
        product_analysis["Sales"].idxmax(),
        "Product_Name"
    ]

    best_selling_product_sales = product_analysis["Sales"].max()

    most_profitable_product = product_analysis.loc[
        product_analysis["Profit"].idxmax(),
        "Product_Name"
    ]

    most_profitable_product_profit = product_analysis["Profit"].max()

else:

    best_selling_product = "N/A"
    best_selling_product_sales = 0

    most_profitable_product = "N/A"
    most_profitable_product_profit = 0


# ============================================================
# CATEGORY PERFORMANCE
# ============================================================

category_analysis = (
    filtered_df
    .groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
)


if not category_analysis.empty:

    best_category_row = category_analysis.loc[
        category_analysis["Sales"].idxmax()
    ]

    best_category = best_category_row["Category"]

    best_category_sales = best_category_row["Sales"]

    highest_profit_category = category_analysis.loc[
        category_analysis["Profit"].idxmax(),
        "Category"
    ]

    highest_category_profit = category_analysis["Profit"].max()

else:

    best_category = "N/A"
    best_category_sales = 0

    highest_profit_category = "N/A"
    highest_category_profit = 0


# ============================================================
# REGION PERFORMANCE
# ============================================================

region_analysis = (
    filtered_df
    .groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)


if not region_analysis.empty:

    best_region_row = region_analysis.loc[
        region_analysis["Sales"].idxmax()
    ]

    best_region = best_region_row["Region"]

    best_region_sales = best_region_row["Sales"]

else:

    best_region = "N/A"
    best_region_sales = 0


# ============================================================
# CUSTOMER PERFORMANCE
# ============================================================

customer_analysis = (
    filtered_df
    .groupby("Customer_Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
)


if not customer_analysis.empty:

    top_customer_row = customer_analysis.loc[
        customer_analysis["Sales"].idxmax()
    ]

    top_customer = top_customer_row["Customer_Name"]

    top_customer_sales = top_customer_row["Sales"]

else:

    top_customer = "N/A"
    top_customer_sales = 0


# ============================================================
# PAYMENT METHOD PERFORMANCE
# ============================================================

payment_analysis = (
    filtered_df
    .groupby("Payment_Method")
    .agg(
        Sales=("Sales", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
)


if not payment_analysis.empty:

    top_payment_row = payment_analysis.loc[
        payment_analysis["Sales"].idxmax()
    ]

    top_payment = top_payment_row["Payment_Method"]

    top_payment_sales = top_payment_row["Sales"]

else:

    top_payment = "N/A"
    top_payment_sales = 0


# ============================================================
# INSIGHT CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📅 Best Sales Month",
        best_month,
        f"₹{best_month_sales:,.0f}"
    )


with col2:

    st.metric(
        "🏆 Best-Selling Product",
        best_selling_product,
        f"₹{best_selling_product_sales:,.0f}"
    )


with col3:

    st.metric(
        "💰 Most Profitable Product",
        most_profitable_product,
        f"₹{most_profitable_product_profit:,.0f}"
    )


with col4:

    st.metric(
        "🌎 Best Region",
        best_region,
        f"₹{best_region_sales:,.0f}"
    )


col5, col6, col7, col8 = st.columns(4)


with col5:

    st.metric(
        "🏷️ Best Category",
        best_category,
        f"₹{best_category_sales:,.0f}"
    )


with col6:

    st.metric(
        "📈 Highest Profit Category",
        highest_profit_category,
        f"₹{highest_category_profit:,.0f}"
    )


with col7:

    st.metric(
        "👑 Top Customer",
        top_customer,
        f"₹{top_customer_sales:,.0f}"
    )


with col8:

    st.metric(
        "💳 Top Payment Method",
        top_payment,
        f"₹{top_payment_sales:,.0f}"
    )


# ============================================================
# BUSINESS SUMMARY
# ============================================================

st.subheader("📋 Business Summary")


summary_col1, summary_col2 = st.columns(2)


with summary_col1:

    st.info(
        f"""
        **📈 Revenue Performance**

        • Best sales month: **{best_month}**

        • Best-selling product: **{best_selling_product}**

        • Best category: **{best_category}**

        • Best-performing region: **{best_region}**
        """
    )


with summary_col2:

    st.success(
        f"""
        **💰 Profit & Customer Performance**

        • Most profitable product: **{most_profitable_product}**

        • Highest-profit category: **{highest_profit_category}**

        • Top customer: **{top_customer}**

        • Leading payment method: **{top_payment}**
        """
    )


# ============================================================
# LOW MARGIN PRODUCTS
# ============================================================

st.subheader("⚠️ Low-Margin Products")


margin_analysis = (
    filtered_df
    .groupby("Product_Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)


margin_analysis["Profit_Margin"] = (
    margin_analysis["Profit"]
    / margin_analysis["Sales"]
    * 100
)


low_margin_products = (
    margin_analysis
    .sort_values(
        "Profit_Margin",
        ascending=True
    )
    .head(10)
)


if not low_margin_products.empty:

    fig_low_margin = px.bar(
        low_margin_products.sort_values(
            "Profit_Margin"
        ),
        x="Profit_Margin",
        y="Product_Name",
        orientation="h",
        title="10 Products with Lowest Profit Margin",
        text_auto=".2f"
    )

    fig_low_margin.update_layout(
        xaxis_title="Profit Margin (%)",
        yaxis_title="Product"
    )

    st.plotly_chart(
        fig_low_margin,
        width="stretch"
    )


# ============================================================
# SALES PERFORMANCE TABLE
# ============================================================

st.subheader("📊 Category Performance Summary")


category_summary = (
    filtered_df
    .groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Cost=("Cost", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum"),
        Orders=("Order_ID", "nunique")
    )
    .reset_index()
)


category_summary["Profit_Margin"] = (
    category_summary["Total_Profit"]
    / category_summary["Total_Sales"]
    * 100
)


category_summary = category_summary.sort_values(
    "Total_Sales",
    ascending=False
)


st.dataframe(
    category_summary,
    width="stretch",
    hide_index=True
)

st.markdown(
    '<div class="section-title">💡 Business Insights</div>',
    unsafe_allow_html=True
)


best_category = (
    category_sales.iloc[0]["Category"]
    if not category_sales.empty
    else "N/A"
)

best_region = (
    region_sales.iloc[0]["Region"]
    if not region_sales.empty
    else "N/A"
)

best_product = (
    top_products.iloc[0]["Product_Name"]
    if not top_products.empty
    else "N/A"
)

best_payment = (
    payment_sales.iloc[0]["Payment_Method"]
    if not payment_sales.empty
    else "N/A"
)


insight_col1, insight_col2 = st.columns(2)


with insight_col1:

    st.info(
        f"🏷️ **Best Category:** {best_category}\n\n"
        f"🌎 **Best Region:** {best_region}\n\n"
        f"🏆 **Top Product:** {best_product}"
    )


with insight_col2:

    st.success(
        f"💳 **Top Payment Method:** {best_payment}\n\n"
        f"💰 **Total Revenue:** ₹{total_sales:,.2f}\n\n"
        f"📈 **Profit Margin:** {profit_margin:.2f}%"
    )


# ============================================================
# FILTERED DATA TABLE
# ============================================================

st.markdown(
    '<div class="section-title">📋 Filtered Sales Data</div>',
    unsafe_allow_html=True
)


display_columns = [
    "Order_ID",
    "Order_Date",
    "Customer_Name",
    "Product_Name",
    "Category",
    "Region",
    "State",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit",
    "Payment_Method"
]


st.dataframe(
    filtered_df[display_columns],
    width="stretch",
    height=450
)


# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_sales_data.csv",
    mime="text/csv",
    width="stretch"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <b>Sales & Revenue Analysis Dashboard</b><br>
        Built with Python • Pandas • Plotly • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)