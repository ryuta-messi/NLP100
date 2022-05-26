from collections import defaultdict
from answer30 import sentences

ans = defaultdict(int)
for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            ans[morph['surface']] += 1
            

ans = sorted(ans.items(),key=lambda x:x[1],reverse=True)

for word in ans[:5]:
    print(word)