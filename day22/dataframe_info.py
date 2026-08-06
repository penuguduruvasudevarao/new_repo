import pandas as pd

# Read the CSV file
df = pd.read_csv("student.csv")

# Display the complete DataFrame
print(df)

print("\n----- INFO -----")
df.info()

print("\n----- DESCRIPTION -----")
print(df.describe())

print("\n----- SHAPE -----")
print(df.shape)

print("\n----- COLUMNS -----")
print(df.columns)