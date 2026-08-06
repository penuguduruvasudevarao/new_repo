import pandas as pd

df=pd.read_csv("student.csv")

print("Names :")
print(df["Name"])

print("\n Marks")
print(df["Marks"])

print("\n Name and Marks")
print(df[["Name","Marks"]])