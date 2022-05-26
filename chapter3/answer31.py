from answer30 import sentences


ans = set()
for sentence in sentences: ## ex sentences {'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'},
    for morph in sentence:
        if morph['pos'] == '動詞':
            ans.add(morph['surface']) ##set Only non-duplicate elements will be retained.
            

print(f'動詞の表層形の種類:{len(ans)}\n')
print(f'samples')

for v in list(ans)[:5]:
    print(v)