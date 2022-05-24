from turtle import pen
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

X_train = pd.read_table('train.feature.txt',header=None)
y_train = pd.read_table('train.txt',header=None)[1]

model = LogisticRegression(random_state=0)
model.fit(X_train,y_train)

joblib.dump(model,'model.joblib')

