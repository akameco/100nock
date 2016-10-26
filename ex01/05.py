# coding=utf-8

def ngram(input, n):
    last = len(input) - n + 1
    return [input[i:i+n] for i in range(0, last)]

str = "I am an NLPer"
print(ngram(str))
print(ngram(str.split()))
