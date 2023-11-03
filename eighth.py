import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

print(cancer_data.keys())

print(cancer_data['DESCR'])

df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])
print(df.head())