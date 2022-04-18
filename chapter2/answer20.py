import pandas as pd


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df["title"]=="イギリス"]["text"].values[0]

print(uk_text)