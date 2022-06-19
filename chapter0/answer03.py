import re
text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

text = re.sub('[,\.]','',text)
splited_text = text.split()
ans = [len(word) for word in splited_text]
print(ans)