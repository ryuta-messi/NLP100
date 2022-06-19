import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict
from answer30 import sentences


ans = defaultdict(int)
for sentence in sentences:
    if '猫' in [morph['surface'] for morph in sentence]:
        for morph in sentence:
            if morph['pos'] != '記号' and morph['pos'] !='助詞':
                ans[morph['surface']] +=1
                
del ans['猫']

ans = sorted(ans.items(),key=lambda x:x[1], reverse=True)

words = [element[0] for element in ans[:10]]
counts = [element[1] for element in ans[:10]]

plt.figure(figsize=(10,6))
plt.bar(words,counts)
plt.show()