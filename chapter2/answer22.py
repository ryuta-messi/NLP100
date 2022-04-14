import pandas as pd
df = pd.read_json("chapter2/jawiki-country.json.gz",lines=True)

uk_article = df[df['title']=="イギリス"]['text'].values[0]
uk_text = uk_article.split('\n')
ans = list(filter(lambda x: '[Category:' in x ,uk_text))
ans = [a.replace("[[Category:","").replace("|*","").replace("]]","") for a in ans]
print(list(ans))