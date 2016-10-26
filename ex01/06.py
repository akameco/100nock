# coding=utf-8
def ngram(input, n):
    last = len(input) - n + 1
    return [input[i:i+n] for i in range(0, last)]

str1 = 'paraparaparadise'
str2 = 'paragraph'

X, Y = set([ngram(x, 2) for x in [str1, str2]])

print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))

print('se' in X)
print('se' in Y)
