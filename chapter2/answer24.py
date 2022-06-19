import re
import pandas as pd


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df["title"]=="イギリス"]["text"].values[0]

for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]',uk_text):
    print(file)
    
    
## revise later
