import re
import pandas as pd
from typing import Dict


def remove_stress(dic:Dict) -> Dict:
    r = re.compile("'+")
    return {key:r.sub('',value) for key, value in dic.items()}


def remove_inner_links(dic:Dict) -> Dict:
    r = re.compile('\[\[(.+\||)(.+?)\]\]')
    return {key:r.sub(r'\2',value) for key,value in dic.items()}


def remove_mk(v:str) -> str:
    r1 = re.compile("'+")
    r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
    r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
    r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')
    
    v = r1.sub('',v)
    v = r2.sub(r'\2',v)
    v = r3.sub(r'\2',v)
    v = r4.sub('',v)
    
    return v


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df['title']=="イギリス"]['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in uk_texts:
    r = re.search(pattern,line)
    if r:
        ans[r[1]] = r[2]
        
r = re.compile('\[\[(.+\||)(.+?)\]\]')
ans = {key:r.sub(r'\2',remove_mk(value)) for key,value in ans.items()}
print(remove_inner_links(remove_stress(ans)))