#!/usr/bin/env python3
import sys

count = 0
countList = []
# input comes from STDIN
for line in sys.stdin:
    if count == 10:
        break

    line = line.strip().split('\t')
    countList.append([line[0],line[1]])

for item in reversed(countList):
    print('%s\t%s' % ( item[0] , item[1] ))