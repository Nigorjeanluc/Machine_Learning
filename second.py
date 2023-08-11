import pandas as pd

df = pd.read_csv('titanic.csv')

col = df['Fare']

# print('CSV: ', df)

# this is a data series
print(col)

# this is a small data frame from the main data frame
small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head())

# creating a column is a passenger is a male or not
df['male'] = df['Sex'] == 'male'
print(df.head())