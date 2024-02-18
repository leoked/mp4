#!/usr/bin/env python3
import sys

countList = dict()
# input comes from STDIN
for line in sys.stdin:
        line = line.strip().split('\t')
        countList[line[0]] = int(line[1])

sortD = dict(sorted(countList.items(), key = lambda item: item[1]))

for w in sortD:
        print('%s\t%s' % ( w , sortD[w] ))