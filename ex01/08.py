# coding=utf-8

def alf(x):
    if x > 96 and x < 123:
        return chr(219 -x)
    else:
        return chr(x)
def cipher(input):
    return ''.join([alf(ord(x)) for x in input])

print(cipher('Hello World'))
