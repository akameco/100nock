# coding=utf-8
str1 = "パトカー"
str2 = "タクシー"

str = ''.join([a + b for a,b in zip(str1, str2)])
print(str)
