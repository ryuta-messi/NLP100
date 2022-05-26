import pandas as pd
import joblib
# from sklearn.linear_model import LogisticRegression

# X_train = pd.read_table('train.feature.txt',header=None)
# y_train = pd.read_table('train.txt',header=None)[1]
X_test = pd.read_table('test.feature.txt')

model = joblib.load('model.joblib')

test_prediction = model.predict(X_test)

print(test_prediction)
