# coding=utf-8

with open('hightemp.txt') as f:
    for line in f:
        print(line.replace("\n", ' '))
