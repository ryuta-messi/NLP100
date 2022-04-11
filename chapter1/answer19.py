from os import sep
import pandas as pd

df = pd.read_csv('chapter1/popular-names.txt',header=None,sep='\t')
print(df[0].value_counts())