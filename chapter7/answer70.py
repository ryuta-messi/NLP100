import numpy as np
import pandas as pd
import joblib
from gensim.models import KeyedVectors
from tqdm import tqdm

def culcWordEmb(row):
    global model
    word_vec = [model[w] if w in model.key_to_index else np.zeros(shape=(model.vector_size)) for w in row['TITLE'].split()]
    word_vec = np.mean(np.array(word_vec),axis=0)
    return word_vec

X_train = pd.read_table('chapter5/train.txt',header=None)
X_valid = pd.read_table('chapter5/valid.txt',header=None)
X_test = pd.read_table('chapter5/test.txt',header=None)

used_columns = ['TITLE','CATEGORY']

X_train.columns = used_columns
X_valid.columns = used_columns
X_test.columns = used_columns
# print(X_test)
n_train = len(X_train)
n_valid = len(X_valid)
n_test = len(X_test)

data = pd.concat([X_train,X_valid,X_test]).reset_index(drop = True)

model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz', binary=True)
tqdm.pandas()
sum_word_vec = data.apply(culcWordEmb,axis=1)


X_train = np.array(list(sum_word_vec.values))[:n_train]
X_valid = np.array(list(sum_word_vec.values))[n_train:n_train+n_valid]
X_test = np.array(list(sum_word_vec.values))[n_train+n_valid:]

print(X_train[:10])

# joblib.dump(X_train,'chapter7/X_train.joblib')
# joblib.dump(X_valid,'chapter7/X_valid.joblib')
# joblib.dump(X_test,'chapter7/X_test.joblib')

y_data = data['CATEGORY']

y_train = y_data.values[:n_train]
y_valid = y_data.values[n_train:n_train + n_valid]
y_test = y_data.values[n_train+n_valid:]

joblib.dump(y_train,'chapter7/y_train.joblib')
joblib.dump(y_valid,'chapter7/y_valid.joblib')
joblib.dump(y_test,'chapter7/y_test.joblib')

print(y_train)