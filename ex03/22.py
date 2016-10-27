# coding=utf-8
import re

for line in open('./uk.txt'):
    r = re.search(re.compile('\[\[Category:(.+?)\]\]'), line)
    if r:
        print(r.group(1))
