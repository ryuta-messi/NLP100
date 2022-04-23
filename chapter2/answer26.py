import re
import pandas as pd

def remove_stress(dic):
    r = re.compile("'+")
    return {key:r.sub('',value) for key , value in dic.items()}


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df['title']=='イギリス']['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}

for line in uk_texts:
    r = re.search(pattern,line)
    if r:
        ans[r[1]] = r[2]
print(remove_stress(ans))


## revise later