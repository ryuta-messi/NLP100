from answer30 import sentences

ans = set()
for sentence in sentences: ##ex sentences {'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'},
    for morph in sentence:
        if morph['pos'] == '動詞':
            ans.add(morph['base'])
            
print(f'動詞の原形の種類:{len(ans)}')
print('samples')
for v in list(ans)[:5]:
    print(v)