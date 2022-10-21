TEXT = data.Field(sequential=True,lower=True,batch_first=True)
LABELS = data.Field(sequential=False,batch_first=True,use_vocab=False)

train,val,test = data.TabularDataset.splits(
    path='chapter5',
    train='train.txt',
    validation='valid.txt',
    test='test.txt',
    format='tsv',
    fields=[('text',TEXT),('label',LABELS)])

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
train_iter,val_iter,test_iter = data.Iterator.splits(
    (train,val,test),batch_sizes=(64,64,64),device=device,repeat=False,sort=False
    )

TEXT.build_vocab(train,min_freq=2)
LABELS.build_vocab(train)
model = RNN(len(TEXT.vocab.stoi)+1,num_layers=2,output_size=4)

for epoch in range(1):
    model.train()
    for batch in train_iter:
        x,y = batch.text,batch.label
        y_pred = model(x)
        print(y_pred)
        print(y_pred.shape)
