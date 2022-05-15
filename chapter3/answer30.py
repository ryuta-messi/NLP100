filename ="chapter3/neko.txt.mecab" 

sentences =[]
morphs = []

with open(filename,mode="r") as f:
    for line in f:
        if line != 'EOS\n':
            blocks = line.split('\t')
            if blocks[0] == '' or len(blocks) != 2: ## blocks = ['', '記号,一般,*,*,*,*,*\n'] or ['\n] -->len 1 or  ['吾輩','名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ'] len -->2
                continue
            else:
                attr = blocks[1].split(',')
                morph = {'surface':blocks[0],'base':attr[6],'pos':attr[0],'pos1':attr[1]}
                morphs.append(morph)
        else:
            sentences.append(morphs)
            morphs = []

# for morph in sentences[2]:
#     print(morph)
if __name__ == '__main__':
    print(len(sentences))