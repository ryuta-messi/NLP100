import sys 
import pandas as pd


if len(sys.argv) == 1:
    print('Set arg n, like "python3 chapter1/answer15.py 5"')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('chapter1/popular-names.txt',sep='\t',header=None,names=['name', 'sex', 'number', 'year'])
    nrow = -(-len(df)//n) ## math.ceilを使わない切り上げ -11//3 --> -4  11//3 -->3
    
    for i in range(n):
        df.iloc[nrow*i:nrow*(i+1)].to_csv(f'chapter1/answer16_{i}',sep='\t',index=False,header=None) ##なぜエラーにならない？　最後のループでindexがDataFrameの長さを超えるてエラーになると思った
    