import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('titanic.csv')

# scattered graph
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])

# labels
plt.xlabel('Age')
plt.ylabel('Fare')

plt.plot([0, 80], [85, 5])

plt.show()
