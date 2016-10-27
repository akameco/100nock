# coding=utf-8
# cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -r
from collections import Counter

arr = [x.rstrip().split('\t')[0] for x in open('./hightemp.txt')]

for word, c in Counter(arr).most_common():
    print(c, word)

# d = {}
# for x in arr:
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1

# for x in sorted(d.items(), key=itemgetter(1)):
#     print(x[0])
