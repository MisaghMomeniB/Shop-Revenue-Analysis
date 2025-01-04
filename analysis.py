import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file containing sales data into a DataFrame
data = pd.read_csv("sales-data.csv")

# Basic Information: Summarizing the dataset
# This dictionary provides a quick summary of the dataset's overall structure and key statistics
basic_info = {
    "Total Products": data.shape[0],
    "Categories": data["Category"].nunique(),
    "Suppliers": data["Supplier"].nunique(),
    "Average Price": data["Price"].mean(),
    "Average Stock": data["Stock"].mean()
}
print("Basic Information:\n", basic_info)

# Analysis: Counting the number of products per supplier
supplier_distribution = data["Supplier"].value_counts()

# Price and Stock Extremes: Identifying products with the highest and lowest price and stock
# This helps understand the outliers and range of values in the dataset
extremes = {
    "Most Expensive Product": data.loc[data["Price"].idxmax()].to_dict(),
    "Least Expensive Product": data.loc[data["Price"].idxmin()].to_dict(),
    "Highest Stock Product": data.loc[data["Stock"].idxmax()].to_dict(),
    "Lowest Stock Product": data.loc[data["Stock"].idxmin()].to_dict()
}
print("\nExtremes:\n", extremes)

# Correlation Analysis: Examining relationships between price and stock
correlation = data[["Price", "Stock"]].corr()

# Visualization Helper Function for reusable plotting
# This helper function standardizes the process of creating visualizations to avoid repetitive code
def plot_chart(title, xlabel, ylabel, chart_func, **kwargs):
    plt.figure(figsize=(12, 6))
    chart_func(**kwargs)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Price Distribution Visualization
plot_chart(
    "Price Distribution", "Price", "Frequency", 
    sns.histplot, data=data["Price"], kde=True, bins=20, color="blue"
)

# Product Distribution by Category Visualization
category_distribution = data["Category"].value_counts()
plot_chart(
    "Product Distribution by Category", "Category", "Number of Products", 
    sns.barplot, x=category_distribution.index, y=category_distribution.values, palette="viridis"
)

# Supplier Distribution Visualization
plot_chart(
    "Products by Supplier", "Supplier", "Number of Products", 
    sns.barplot, x=supplier_distribution.index, y=supplier_distribution.values, palette="cool"
)

# Correlation Heatmap Visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Price Distribution by Category Visualization
plot_chart(
    "Price Distribution by Category", "Category", "Price", 
    sns.boxplot, x="Category", y="Price", data=data, palette="Set2"
)

# Price vs Stock Scatterplot
plot_chart(
    "Price vs Stock", "Price", "Stock", 
    sns.scatterplot, x="Price", y="Stock", data=data, hue="Category", palette="deep", s=100
)

# Category Pie Chart Visualization
plt.figure(figsize=(8, 8))
category_distribution.plot(kind="pie", autopct="%1.1f%%", startangle=140, colormap="Set3")
plt.title("Category Distribution", fontsize=14)
plt.ylabel("")
plt.show()

# Summary Report: Merging all extreme values and correlation data into a single report
summary_report = {**extremes, "Correlation (Price vs Stock)": correlation.to_dict()}
print("\nSummary Report:\n", summary_report)