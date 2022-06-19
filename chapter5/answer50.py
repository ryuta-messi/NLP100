from operator import index
from random import random
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('newsCorpora_re.csv',
                 header=None,
                 sep='\t',
                 names=[
                     'ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY',
                     'HOSTNAME', 'TIMESTAMP'
                 ])

df = df[df['PUBLISHER'].isin([
    'Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com',
    'Daily Mail'
])].sample(
    frac=1, random_state=0
)  ##pandas.Series.sample()はデータセットから指定した割合を抽出する処理で、抽出率を100%にすることでランダム並び替えと同等の処理
print(df.head)
#ニュース記事の見出しを「ビジネス」「科学技術」「エンターテイメント」「健康」のカテゴリに分類するタスク（カテゴリ分類）
X = df[['TITLE', 'CATEGORY']]
X['CATEGORY'] = X['CATEGORY'].map({'b': 0, 'e': 1, 't': 2, 'm': 3})
y = df['CATEGORY']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=0)
X_valid, X_test, y_valid, y_test = train_test_split(X_test,y_test,test_size=0.5,stratify=y_test,random_state=0)

X_train.to_csv('train.txt', sep='\t', index=False, header=None)
X_test.to_csv('test.txt', sep='\t', index=False, header=None)
X_valid.to_csv('valid.txt', sep='\t', index=False, header=None)

#y_train.to_csv('test_a.txt',sep='\t',index=False,header=None) 
