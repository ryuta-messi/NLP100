import pandas as pd
<<<<<<< HEAD
df = pd.read_json("chapter2/jawiki-country.json.gz",lines=True)

uk_article = df[df['title']=="イギリス"]['text'].values[0]
uk_text = uk_article.split('\n')
ans = list(filter(lambda x: '[Category:' in x ,uk_text))
ans = [a.replace("[[Category:","").replace("|*","").replace("]]","") for a in ans]
print(list(ans))
=======


df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df["title"]=="イギリス"]["text"].values[0]

uk_texts = uk_text.split('\n')
ans = list(filter(lambda x : '[Category' in x,uk_texts))

ans = [a.replace('[[Category:','').replace('|*','').replace(']]','') for a in ans]

print(ans)
>>>>>>> 51a5fcd4c1934fbf831a79edea7d115efa700a65
