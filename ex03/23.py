# coding=utf-8
import re

for line in open('./uk.txt'):
    r = re.search(r"^(=+)(.+?)(=+)", line)
    if r:
        e = r.groups()
        print(len(e[0]) - 1, e[1])
