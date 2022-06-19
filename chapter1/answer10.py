import pandas as pd

df = pd.read_table("chapter1/popular-names.txt",header=None, sep='\t', names=['name', 'sex', 'number', 'year'])
print(len(df))