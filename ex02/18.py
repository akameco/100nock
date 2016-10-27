# coding=utf-8
# sort -r -k 2 hightemp.txt
from operator import itemgetter

arr = [line.rstrip().split('\t') for line in open('./hightemp.txt')]
sorted_arr = sorted(arr, key=itemgetter(2), reverse=True)
for line in sorted_arr:
    print('\t'.join(line))
