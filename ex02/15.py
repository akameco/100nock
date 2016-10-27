# coding=utf-8
import sys

n = int(sys.argv[1])

with open('./hightemp.txt') as f:
    for line in f.read().split('\n')[-(n + 1):]:
        print(line)
