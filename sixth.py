import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic.csv')

df['male'] = df['Sex'] == 'male'

X = df[[
    'Pclass',
    'male',
    'Age',
    'Siblings/Spouses',
    'Parents/Children',
    'Fare'
]].values

y = df['Survived'].values

# print(X)
# print(y)

model = LogisticRegression()
model.fit(X, y)

# print(model.coef_, model.intercept_)

# # scattered graph
# plt.scatter( df['Fare'], df['Age'], c=df['Pclass'])

# # labels
# plt.xlabel('Age')
# plt.ylabel('Fare')

# plt.plot([0, 80], [85, 5])

# plt.show()

model.predict(X)

# The first passenger in the dataset is:
# print(X[0])

# predict is the first passenger has survived
print(model.predict([X[0]]))

# predict is the first five passengers have survived
print(model.predict(X[:5]))

# the data of first five passengers for those who survirved or not
print(y[:5])