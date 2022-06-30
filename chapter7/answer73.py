import joblib
import numpy as np
import torch 
from torch import nn,optim



X_train = joblib.load('chapter7/X_train.joblib')
y_train = joblib.load('chapter7/y_train.joblib')

X_train = torch.from_numpy(X_train.astype(np.float32)).clone()
y_train = torch.from_numpy(y_train.astype(np.int64)).clone()

# print(X_train.size())

X = X_train[0:4]
y = y_train[0:4]

# print(X.size())
net = nn.Linear(X.size()[1],4)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr=0.01)

losses = []
print(y)
for epoc in range(100):
    optimizer.zero_grad()
    y_pred = net(X)
    loss = loss_fn(y_pred,y)
    loss.backward()
    optimizer.step()
    losses.append(loss)

# print(net.state_dict()['weight'])