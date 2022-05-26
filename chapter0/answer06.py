from answer05 import n_gram

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(n_gram(2, str1))
Y = set(n_gram(2, str2))

union = X | Y
intersection = X & Y
difference = X-Y

print('和集合:', union)
print('積集合:', intersection)
print('差集合:', difference)
