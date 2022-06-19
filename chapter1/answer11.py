import pandas as pd

df = pd.read_csv('chapter1/popular-names.txt',sep="\t",header=None)
df.to_csv('chapter1/ans11.txt',sep=" ",index=False,header=None)