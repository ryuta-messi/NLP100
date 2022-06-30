import joblib
import numpy as np
import torch 
from torch import nn,optim

X_train = joblib.load('chapter7/X_train.joblib')
y_train = joblib.load('chapter7/y_train.joblib')
X_train = torch.from_numpy(X_train.astype(np.float32)).clone()
y_train = torch.from_numpy(y_train.astype(np.int64)).clone()


X_test = joblib.load('chapter7/X_test.joblib')
y_test = joblib.load('chapter7/y_test.joblib')
X_test = torch.from_numpy(X_test.astype(np.float32)).clone()
y_test = torch.from_numpy(y_test.astype(np.int64)).clone()

X = X_train
y = y_train

net = nn.Linear(X.size()[1],4)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr=0.01)

losses = []

for epoc in range(100):
    optimizer.zero_grad()
    y_pred = net(X)
    loss = loss_fn(y_pred,y)
    loss.backward()
    optimizer.step()
    losses.append(loss)


_,y_pred_train = torch.max(net(X),axis=1)
print((y_pred_train == y).sum().item() / len(y))

_,y_pred_test = torch.max(net(X_test),axis=1)
print((y_pred_test == y_test).sum().item()/len(y_test))

# >>> a = torch.randn(4, 4)
# >>> a
# tensor([[-1.2360, -0.2942, -0.1222,  0.8475],
#         [ 1.1949, -1.1127, -2.2379, -0.6702],
#         [ 1.5717, -0.9207,  0.1297, -1.8768],
#         [-0.6172,  1.0036, -0.6060, -0.2432]])
# >>> torch.max(a, 1)
# torch.return_types.max(values=tensor([0.8475, 1.1949, 1.5717, 1.0036]), indices=tensor([3, 0, 0, 1]))
#return value1 torch.return_types.max(values=tensor([0.8475, 1.1949, 1.5717, 1.0036])
#return value2 indices=tensor([3, 0, 0, 1]))