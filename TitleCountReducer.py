#!/usr/bin/env python3
from operator import itemgetter
import sys

wordDict = dict()

# input comes from STDIN
for line in sys.stdin:
    line = line.strip().split('\t')
    
    if line[0] in wordDict:
        wordDict[line] += 1
    else:
        wordDict[line] = 1

for w in wordDict:
    print('%s\t%s' % ( w , wordDict[w] )) 