from answer30 import sentences

ans = set()
for sentence in sentences:
    nouns = ''
    count = 0
    for morph in sentence:
        if morph['pos']=='名詞':
            nouns = ''.join([nouns,morph['surface']])
            count += 1
        elif count >= 2:
            ans.add(nouns)
            count = 0
            nouns = ''
        else:
            count = 0
            nouns =''
    if count >= 2:
        ans.add(nouns)
        
        
            
print(f'連接名詞の種類: {len(ans)}\n')
print('samples')
print(list(ans)[:5])