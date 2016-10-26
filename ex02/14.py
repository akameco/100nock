# coding=utf-8
import sys
n = int(sys.argv[1])

with open('./hightemp.txt') as f:
    for line, i in zip(f, range(n)):
        if i > n:
            break
        print(line)
