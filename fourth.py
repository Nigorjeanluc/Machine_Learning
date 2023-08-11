import pandas as pd
df = pd.read_csv('titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
# 2nd column of the 1st row
print(arr[0, 1])

# whole 1st row
print(arr[0])

# whole 3rd column
print(arr[:,2])

# take first 10 values for simplicity
arr = df[['Pclass', 'Fare', 'Age']].values[:10]

# masking i.e selecting all passengers under the age of 18
mask = arr[:, 2] < 18
print(arr[mask])
# or print(arr[arr[:, 2] < 18])

# summing or counting
print("Sum of children: ", mask.sum())
# or print((arr[:, 2] < 18).sum())