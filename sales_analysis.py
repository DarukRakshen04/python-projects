import pandas as pd

data = {
    "product": ["A", "B", "A", "C"],
    "price": [100, 200, 100, 300],
    "quantity": [2, 1, 3, 1]
}

df = pd.DataFrame(data)

df["total"] = df["price"] * df["quantity"]

print("Total Revenue:", df["total"].sum())
print(df.groupby("product")["total"].sum())
