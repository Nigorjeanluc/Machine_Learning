import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic.csv')

df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

# print(y)

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)

# All passanger
print(y.shape[0])

# Well predicted survival passenger
print((y == y_pred).sum())

# Thus our accuracy score is computed as follows
print((y == y_pred).sum() / y.shape[0])

# we can get the same result by using the score method

print(model.score(X, y))