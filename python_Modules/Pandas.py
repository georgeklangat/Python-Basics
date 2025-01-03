# pandas -python Data Analysis or python panel
# Pandas is a powerful Python library designed for data manipulation and analysis. It provides two primary data structures:
# Series - A one-dimensional labeled array(indexed).
# DataFrame - A two-dimensional labeled data structure like a table.

# 1. Series
import pandas as pd
data = [1,2,3,4,5,6,7]
series = pd.Series(data)
print(series)

# series with custom labels
data1 = [23,45,23]
series1 = pd.Series(data1,index = ["x","y","z"])
print(series1)

# 2. DataFrame
# Dictionary data
data2 = {
     "car":["BMW","VOLVO","MERCEDES"],
    "passing": [11,21,30]
 }
df = pd.DataFrame(data2)
print(df)
print(df.loc[0]) # accessing the 1st row
print(df.iloc[0:]) # accessing all the rows

print(df.info()) # give more information about the dataframe
print(df.tail(3)) # -return headers and specified number of rows from the bottom
print(df.head(1)) # return headers and specified number of row from the top