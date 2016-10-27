# coding=utf-8
with open('./hightemp.txt') as f:
    col1 = [line.split('\t')[0] for line in f.read().rstrip().split('\n')]
    print(len(set(col1)))
