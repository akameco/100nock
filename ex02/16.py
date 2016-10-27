# coding=utf-8
import sys
n = int(sys.argv[1])

with open('./hightemp.txt') as f:
    arr = f.read().rstrip().split('\n')
    step = int(len(arr) / n) + 1
    for i in range(step):
        with open('./x-{}'.format(str(i)), 'w') as of:
            c = i * n
            of.write('\n'.join(arr[c:c+n]))
