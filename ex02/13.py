# coding=utf-8

f1 = open('./col1.txt')
f2 = open('./col2.txt')

for col1, col2 in zip(f1, f2):
    print("{}\t{}".format(col1.rstrip(), col2.rstrip()))

f1.close()
f2.close()
