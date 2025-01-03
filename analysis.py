import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "sales-data.csv"
data = pd.read_csv(file_path)

# Basic Info
print("Basic Information")
basic_info = {
    "Total Products": data.shape[0],
    "Categories": data["Category"].nunique(),
    "Suppliers": data["Supplier"].nunique(),
    "Average Price": data["Price"].mean(),
    "Average Stock": data["Stock"].mean()
}
print(basic_info)

# Analysis: Products by Supplier
supplier_distribution = data["Supplier"].value_counts()

# Analysis: Price and Stock Extremes
most_expensive = data.loc[data["Price"].idxmax()]
least_expensive = data.loc[data["Price"].idxmin()]
high_stock = data.loc[data["Stock"].idxmax()]
low_stock = data.loc[data["Stock"].idxmin()]

print("Most Expensive Product:", most_expensive)
print("Least Expensive Product:", least_expensive)
print("Highest Stock Product:", high_stock)
print("Lowest Stock Product:", low_stock)

# Correlation Analysis
correlation = data[["Price", "Stock"]].corr()

# Visualization: Price Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data["Price"], kde=True, bins=20, color="blue")
plt.title("Price Distribution", fontsize=14)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization: Product Distribution by Category
category_distribution = data["Category"].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=category_distribution.index, y=category_distribution.values, palette="viridis")
plt.title("Product Distribution by Category", fontsize=14)
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

# Visualization: Supplier Distribution
plt.figure(figsize=(12, 6))
sns.barplot(x=supplier_distribution.index, y=supplier_distribution.values, palette="cool")
plt.title("Products by Supplier", fontsize=14)
plt.xlabel("Supplier")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

# Visualization: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Visualization: Price Distribution by Category
plt.figure(figsize=(12, 6))
sns.boxplot(x="Category", y="Price", data=data, palette="Set2")
plt.title("Price Distribution by Category", fontsize=14)
plt.xlabel("Category")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()

# Visualization: Price vs Stock Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Price", y="Stock", data=data, hue="Category", palette="deep", s=100)
plt.title("Price vs Stock", fontsize=14)
plt.xlabel("Price")
plt.ylabel("Stock")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Visualization: Category Pie Chart
plt.figure(figsize=(8, 8))
category_distribution.plot(kind="pie", autopct="%1.1f%%", startangle=140, colormap="Set3")
plt.title("Category Distribution", fontsize=14)
plt.ylabel("")
plt.show()

# Summary Report
report = {
    "Most Expensive Product": most_expensive.to_dict(),
    "Least Expensive Product": least_expensive.to_dict(),
    "Highest Stock Product": high_stock.to_dict(),
    "Lowest Stock Product": low_stock.to_dict(),
    "Correlation (Price vs Stock)": correlation.to_dict()
}
print("\nSummary Report")
print(report)