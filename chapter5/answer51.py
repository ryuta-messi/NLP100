from operator import index
import joblib
from matplotlib import use
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

X_train = pd.read_table('train.txt',header=None)
X_valid = pd.read_table('valid.txt',header=None)
X_test = pd.read_table('test.txt',header=None)

used_columns = ['TITLE','CATEGORY']

X_train.columns = used_columns
X_valid.columns = used_columns
X_test.columns = used_columns

X_train['TMP'] = 'train'
X_valid['TMP'] = 'valid'
X_test['TMP'] = 'test'

data = pd.concat([X_train,X_valid,X_test]).reset_index(drop=True)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['TITLE'])
data = pd.concat([data,pd.DataFrame(X.toarray())],axis=1)

joblib.dump(vectorizer.vocabulary_,'vocablary_.joblib')

X_train = data[data['TMP'] == 'train'].drop(used_columns + ['TMP'],axis=1) #ベクトルの部分だけが残る
X_valid = data[data['TMP'] == 'valid'].drop(used_columns + ['TMP'],axis=1)
X_test = data[data['TMP'] == 'test'].drop(used_columns + ['TMP'],axis=1)

X_train.to_csv('train.feature.txt',sep='\t',index=False,header=None)
X_valid.to_csv('valid.feature.txt',sep='\t',index=False,header=None)
X_test.to_csv('test.feature.txt',sep='\t',index=False,header=None)
