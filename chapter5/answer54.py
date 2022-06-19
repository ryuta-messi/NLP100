import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

X_train = pd.read_table('train.feature.txt', header=None)
X_test = pd.read_table('test.feature.txt', header=None)
y_train = pd.read_table('train.txt', header=None)[1]
y_test = pd.read_table('test.txt', header=None)[1]

model = joblib.load('model.joblib')

print(f'train accuracy: {accuracy_score(y_train,model.predict(X_train))}')
print(f'test accuracy: {accuracy_score(y_test,model.predict(X_test))}')