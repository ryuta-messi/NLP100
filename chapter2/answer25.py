import re
import pandas as pd

df = pd.read_json('chapter2/jawiki-country.json.gz', lines=True)
uk_text = df[df['title'] == 'イギリス']['text'].values[0]

uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')

ans = {}
for line in uk_texts:
    r = re.search(pattern,line)
    if r:
        ans[r[1]]=r[2]
        
print(ans)


## revise later