# coding=utf-8
import random

def shuffle(x):
    if len(x) <= 4:
        return x
    l = list(x[1:-1])
    random.shuffle(l)
    return x[0] + ''.join(l) + x[-1]

def typoglycemia(s):
    return [shuffle(x) for x in s.split()]

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(str))
