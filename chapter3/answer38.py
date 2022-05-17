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

ans = ans.values()

plt.figure(figsize=(10,6))
plt.hist(ans,bins=100)
plt.xlabel('単語の出現頻度')
plt.ylabel('単語の種類')
plt.show()
