import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Retail_Sales_Performance.csv")

print("\n==== RETAIL SALES ANALYTICS DASHBOARD ===="), print("Developed By: Harshit Singh"), print("\n==== RETAIL SALES ANALYSIS ====\n")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Top Product
top_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_product)

# -------------------------------
# GRAPH 1 : Monthly Sales Trend
# -------------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month_name()

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.show()

# -------------------------------
# GRAPH 2 : Category Wise Sales
# -------------------------------

plt.figure(figsize=(8,5))
sns.barplot(
    x=df.groupby("Category")["Sales"].sum().index,
    y=df.groupby("Category")["Sales"].sum().values
)

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# GRAPH 3 : Region Wise Sales
# -------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7,7))
plt.pie(region_sales,
        labels=region_sales.index,
        autopct="%1.1f%%")

plt.title("Region Wise Sales")
plt.show()

# -------------------------------
# GRAPH 4 : Top Products
# -------------------------------

top5 = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,5))
sns.barplot(x=top5.index, y=top5.values)

plt.title("Top 5 Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=30)

plt.show()

# -------------------------------
# GRAPH 5 : Profit By Category
# -------------------------------

profit_category = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=profit_category.index,
            y=profit_category.values)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# -------------------------------
# GRAPH 6 : City Wise Sales
# -------------------------------

city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(
    x=city_sales.index,
    y=city_sales.values
)

plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()

# -------------------------------
# GRAPH 7 : Quantity vs Profit
# -------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(
    x=df["Quantity"],
    y=df["Profit"],
    hue=df["Category"]
)

plt.title("Quantity vs Profit")
plt.show()

print("\nAnalysis Completed Successfully.")