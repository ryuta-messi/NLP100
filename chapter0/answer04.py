str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str = str.split()
selected_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}
for i,word in enumerate(str):
    if i+1 in selected_list:
        dict[word[0]] = i+1
    else:
        dict[word[:2]] = i+1
print(dict)
        