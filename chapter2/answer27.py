import re 
import pandas as pd
from typing import Dict

def remove_stress(dic:Dict) -> Dict:
    r = re.compile("'+")
    return {key:r.sub('',value) for key, value in dic.items()}


def remove_inner_links(dic:Dict) -> Dict:
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {key:r.sub(r'\2',value) for key,value in dic.items()}

df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df['title']=="イギリス"]['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}

for line in uk_texts:
    r = re.search(pattern,line)
    if r:
        ans[r[1]] = r[2]
print(remove_inner_links(remove_stress(ans)))

## revise later
# \1 ～ \9	一致した文字列の１～９番目に対応する文字列に置換。
