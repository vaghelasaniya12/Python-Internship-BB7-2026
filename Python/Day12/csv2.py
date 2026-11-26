import pandas as pd

df = pd.read_csv("products.csv")

expensive_products = df[df["Price"] > 5000]

print("Products above 5000:")
print(expensive_products)