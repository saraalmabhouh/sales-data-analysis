import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# Clean data
data = data.dropna()

# Calculate total sales per product
product_sales = data.groupby("Product")["Amount"].sum()

print("Total Sales by Product:")
print(product_sales)

# Plot sales chart
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.show()