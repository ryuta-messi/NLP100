import pandas as pd
from gensim.models import KeyedVectors
from tqdm import tqdm


tqdm.pandas()
df = pd.read_csv('chapter6/questions-words.txt', sep=' ')
df = df.reset_index()
df.columns = ['v1', 'v2', 'v3', 'v4']
df.dropna(inplace=True)

model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz', binary=True)
df[['simWord', 'simScore']] = df.progress_apply(lambda row: pd.Series(list(model.most_similar(positive=[row['v2'], row['v3']], negative=[row['v1']])[0])), axis=1)
df.to_csv('chapter6/ans64.txt', sep=' ', index=False, header=None)



