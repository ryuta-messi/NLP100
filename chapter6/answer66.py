import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from tqdm import tqdm


def cosSim(v1,v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))


def culcCosSim(row):
    global model
    vector1 = model[row['Word 1']]
    vector2 = model[row['Word 2']] ## model['word'] ??
    return cosSim(vector1,vector2)


tqdm.pandas()
model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz',binary=True)

df = pd.read_csv('chapter6/combined.csv')
df['cosSim'] = df.progress_apply(culcCosSim,axis=1)

# print(model['love'])
# print(model['sex'])

print(df[['Human (mean)', 'cosSim']].corr(method='spearman'))
print(df.iloc[:10,:])

#vector = word_vectors['computer']  # numpy vector of a word
#similarity = word_vectors.similarity('woman', 'man' )s
