import pandas as pd

student = {
    "Name": ["Vasu", "Rahul", "Arun"],
    "Age": [24, 23, 25],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(student)

print(df["Name"])