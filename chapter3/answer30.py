import MeCab



filename = "./chapter3/neko.txt.mecab"

with open(filename,mode='rt',encoding='utf-8') as f:
    file = f.read()


print(file)
