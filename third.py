import pandas as pd
df = pd.read_csv('titanic.csv')

#one dimension array
print(df['Fare'].values)

#two dimension array
print(df[['Pclass', 'Fare', 'Age']].values)

# we can use numpy to determine the shape of
# our numpy array
arr = df[['Pclass', 'Fare', 'Age']].values
print("Shape (rows, columns): ",arr.shape)