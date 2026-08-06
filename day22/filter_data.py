import pandas as pd 
df= pd.read_csv("student.csv")

print("Students with Marks greater than 90:")
print(df[df["Marks"]>90])

print("\nStudents whose Age is 24:")
print(df[df["Age"] == 24])