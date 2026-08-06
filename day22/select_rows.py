import pandas as pd
df=pd.read_csv("student.csv")
print("First row: ")
print(df.loc[0])

print("\n Third row: ")
print(df.loc[2])