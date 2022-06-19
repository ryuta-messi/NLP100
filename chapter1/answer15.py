import sys
import pandas as pd

if len(sys.argv) == 1:
    print('Set arg n, like "python3 chapter1/answer15.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('chapter1/popular-names.txt',sep='\t',header=None,names=['name', 'sex', 'number', 'year'])
    print(df.tail(n))