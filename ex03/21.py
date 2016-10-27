# coding=utf-8
import re

for line in open('./uk.txt'):
    p = re.compile('\[\[Category')
    if re.search(p, line):
        print(line.strip())
