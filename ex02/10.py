# coding=utf-8

with open('hightemp.txt') as f:
    count = f.read().count('\n')
    print(count)
