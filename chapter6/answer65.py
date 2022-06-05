import pandas as pd

df = pd.read_csv('chapter6/ans64.txt',sep=" ",header=None)
print((df[3] == df[4]).sum()/len(df))