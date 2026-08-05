import pandas as pd

marks=pd.Series([90,85,95],index=['m','S','E'])
print(marks['S'])
print(marks.iloc[0])