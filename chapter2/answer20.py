import pandas as pd
<<<<<<< HEAD
df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_article = df[df['title']=="イギリス"]

print(uk_article)
=======


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df["title"]=="イギリス"]["text"].values[0]

print(uk_text)
>>>>>>> 51a5fcd4c1934fbf831a79edea7d115efa700a65
