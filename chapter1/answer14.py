import sys
import pandas as pd

if len(sys.argv) == 1:
    print('Set arg n, like "python chapter1/answer14.py 14"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv("chapter1/popular-names.txt",sep='\t',header=None)
    print(df.head(n))
    
    
        