import pandas as pd
df = pd.read_csv("chapter1/popular-names.txt",header=None, sep='\t', names=['name', 'sex', 'number', 'year'])

col1 = df['name']
col1.to_csv('chapter1/answer12_col1.txt',index=False)
print(col1.head())

col2 = df['sex']
col2.to_csv('chapter1/answer12_col2.txt',index=False)
print(col2.head())