#!/usr/bin/env python3
import sys

linkDict = dict()

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    if line in linkDict:
        linkDict[line] += 1
    else:
        linkDict[line] = 1

sortD = dict(sorted(linkDict.items(), key = lambda item: item[1],reverse=True))
for w in sortD:
    print('%s\t%s' % ( w , sortD[w] ))