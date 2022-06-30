import numpy as np
import joblib
import torch
import torch.nn as nn


X_train = joblib.load('chapter7/X_train.joblib')
X_train = torch.from_numpy(X_train.astype(np.float32)).clone()

X = X_train[0:4]
# print(X.shape)
# print(X.size())

net = nn.Sequential(nn.Linear(X.size()[1],4),nn.Softmax()) ## torch.Size([4,300]) --> [300,4]
y_pred = net(X)
print(y_pred)