import pandas as pd

df = pd.read_csv('chapter1/popular-names.txt',sep='\t',header=None)
print(len(df[0].unique()))