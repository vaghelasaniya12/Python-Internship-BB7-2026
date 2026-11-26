import pandas as pd

df = pd.read_csv("marks.csv")

average = df["Maths"].mean()

print("Average Maths Marks:", average)

topper_index = df["Maths"].idxmax()

topper = df.loc[topper_index]

print("Maths Topper:")
print("Name:", topper["Student"])
print("Marks:", topper["Maths"])