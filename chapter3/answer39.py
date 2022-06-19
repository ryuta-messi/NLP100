from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib
from answer30 import sentences

ans = defaultdict(int)
for sentence in sentences:
    for morph in sentence:
        if morph['pos'] != '記号':
            ans[morph['surface']] += 1
            
ans = sorted(ans.items(),key=lambda x:x[1],reverse=True)

ranks = [r+1 for r in range(len(ans))]
values = [a[1] for a in ans]

plt.figure(figsize=(10,6))
plt.scatter(ranks,values)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
plt.show()
