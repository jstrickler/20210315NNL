import pandas as pd

for chunk in  pd.read_csv('DATA/titanic3.csv', chunksize=100):
    print(chunk)
    print('=' * 30)
