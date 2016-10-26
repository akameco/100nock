# coding=utf-8

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

arr = str.replace('.', '').replace(',', '').split()
list = [len(x) for x in arr]

print(list)
