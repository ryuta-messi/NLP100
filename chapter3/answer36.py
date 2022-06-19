import matplotlib.pyplot as plt
import japanize_matplotlib
from answer30 import sentences
from collections import defaultdict

ans = defaultdict(int)

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            ans[morph['surface']] += 1

ans = sorted(ans.items(),key=lambda x:x[1],reverse=True)


words = [element[0] for element in ans[0:10]] ## element --> (word,count)
counts = [element[1] for element in ans[0:10]]
print(words)
print(counts)

plt.figure(figsize=(10,6))
plt.bar(words,counts)
plt.show()