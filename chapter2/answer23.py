import re
import pandas as pd

df = pd.read_json('chapter2/jawiki-country.json.gz',lines=True)
uk_text = df[df['title']=='イギリス']['text'].values[0]
for section in re.findall(r'(=+)([^=]+)\1\n',uk_text): ##Returns a tuple with two elements
    # print(section)
    print(f'{section[1].strip()}\t{len(section[0]) -1}')
    
    
    '''
    =+ 任意の数の=
    [^=]+ --> =,==,==== 任意の=以外の文字
    正規表現パターンで括弧()を使ってグルーピングすると、
    各グループの文字列を要素とするタプル（マッチオブジェクトのgroups()に相当）のリストが返される。
    s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'
    result = re.findall(r'([a-z]+)@([a-z]+)\.([a-z]+)', s)
    print(result)
    [('aaa', 'xxx', 'com'), ('bbb', 'yyy', 'com'), ('ccc', 'zzz', 'net')]
    match(/(ABC)(\1)/, "ABCABC")	// 1番目の(...)にマッチした文字列(ABC)にマッチ
    '''