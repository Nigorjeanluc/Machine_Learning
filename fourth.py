import pandas as pd
df = pd.read_csv('titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print("\n")
# 2nd column of the 1st row
print("2nd column of the 1st row")
print(arr[0, 1])
print("\n")

# whole 1st row
print("whole 1st row")
print(arr[0])
print("\n")

# whole 3rd column
print("whole 3rd column")
print(arr[:,2])
print("\n")

# take first 10 values for simplicity
print("take first 10 values for simplicity")
arr = df[['Pclass', 'Fare', 'Age']].values[:10]
print(arr)
print("\n")

# masking i.e selecting all passengers under the age of 18
mask = arr[:, 2] < 18
# print(mask)
print("masking i.e selecting all passengers under the age of 18")
print(arr[mask])
print("\n")
# or print(arr[arr[:, 2] < 18])

# summing or counting
print("summing or counting")
print("Sum of children: ", mask.sum())
print("\n")
# or print((arr[:, 2] < 18).sum())