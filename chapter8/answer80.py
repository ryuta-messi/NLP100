from torchtext import data


TEXT = data.Field(sequential=True, lower=True, batch_first=True)
LABELS = data.Field(sequential=False, batch_first=True, use_vocab=False)

train, valid, test = data.TabularDataset.splits(
    path='chapter5', train='train.txt',
    validation='valid.txt', test='test.txt', format='tsv',
    fields=[('text', TEXT), ('labels', LABELS)])

TEXT.build_vocab(train, min_freq=2)
print(TEXT.vocab.stoi.values())

# print(TEXT)

# print(train)
