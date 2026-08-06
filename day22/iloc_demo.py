import pandas as pd
df=pd.read_csv("student.csv")

print("First row")
print(df.iloc[1])

print("\n Second row :")
print(df.iloc[1])

print("\n Last row :")
print(df.iloc[2])