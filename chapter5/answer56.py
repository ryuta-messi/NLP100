import pandas as pd
import joblib
from sklearn.metrics import recall_score,precision_score,f1_score

# X_train = pd.read_table('train.feature.txt',header=None)
X_test = pd.read_table('test.feature.txt',header=None)
# y_train = pd.read_table('train.txt',header=None)[1]
y_test = pd.read_table('test.txt',header=None)[1]

model = joblib.load('model.joblib')
y_pred = model.predict(X_test)


print(f'test recall of None:{recall_score(y_test,y_pred,average=None)}')
print(f'test precision of None:{precision_score(y_test,y_pred,average=None)}')
print(f'test f1 of None:{f1_score(y_test,y_pred,average=None)}')


# print(f'test f1 of micro:{f1_score(y_test,y_pred,average ="micro")}')
# print(f'test f1 of macro:{f1_score(y_test,y_pred,average ="macro")}')