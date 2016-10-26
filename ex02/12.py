# coding=utf-8

f1 = open('./col1.txt', 'w')
f2 = open('./col2.txt', 'w')

with open('hightemp.txt') as f:
    for line in f:
        col1, col2, tmp, time = line.split('\t')
        f1.write(col1)
        f1.write('\n')
        f2.write(col2)
        f2.write('\n')

f1.close()
f2.close()
