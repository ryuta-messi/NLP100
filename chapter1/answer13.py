import pandas as pd

col1 = pd.read_table("chapter1/popular-names.txt",header=None,names=['name', 'sex', 'number', 'year'])["name"]
col2 = pd.read_table("chapter1/popular-names.txt",header=None,names=['name', 'sex', 'number', 'year'])["sex"]

merged_1_2 = pd.concat([col1,col2],axis=1)
merged_1_2.to_csv('./chapter1/merged_1_2.txt',sep="\t",index=False)
print(merged_1_2.head())

