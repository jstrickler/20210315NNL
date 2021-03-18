import pandas as pd

df = pd.read_csv('DATA/titanic3.csv', dtype={'sex': 'category'})

print(df.head())
print(df.tail())

print(df.describe())
print('-' * 60)
print(df.describe(include='O'))

print(df.info(memory_usage="deep"))



