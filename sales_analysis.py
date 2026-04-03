import pandas as pd
import matplotlib.pyplot as plt

# sample data
data = {
    "product": ["A", "B", "A", "C"],
    "price": [100, 200, 100, 300],
    "quantity": [2, 1, 3, 1]
}

df = pd.DataFrame(data)

# total column
df["total"] = df["price"] * df["quantity"]

print("Total Revenue:", df["total"].sum())

# group by product
product_sales = df.groupby("product")["total"].sum()
print(product_sales)

# plot
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.show()
