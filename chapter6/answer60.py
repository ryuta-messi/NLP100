from gensim.models import KeyedVectors
import joblib
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz',binary=True)
joblib.dump(model,'./model.joblib')
