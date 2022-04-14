import pandas as pd
df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_article = df[df['title']=="イギリス"]

print(uk_article)