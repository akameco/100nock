# coding=utf-8
str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
arr = str.replace('.', '').split()
dict = {}
for a, b in zip(arr[1::2], arr[::2]):
    dict[a[:2]] = a
    dict[b[0]] = b

print(dict)
