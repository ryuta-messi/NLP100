import re
from urllib import request
import requests
import pandas as pd
from answer28 import remove_inner_links,remove_mk,remove_stress

def get_url(dic):
    url_file = dic['国旗画像'].replace(' ','_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file +'&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"',data.text).group(1)

df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df['title']=='イギリス']['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in uk_texts:
    r = re.search(pattern,line)
    if r:
        ans[r[1]] = r[2]

r = re.compile('\[\[(.+\||)(.+?)\]\]')
ans = {key:r.sub(r'\2',remove_mk(value)) for key,value in ans.items()}
print(get_url(remove_inner_links(remove_stress(ans))))