#!/usr/bin/env python3
from operator import itemgetter
import sys

wordDict = dict()

# input comes from STDIN
for line in sys.stdin:
    line = line.strip().split('\t')
    
    if line[0] in wordDict:
        wordDict[line[0]] += 1
    else:
        wordDict[line[0]] = 1
sorted_dict = dict(sorted(wordDict.items(), key=itemgetter(1), reverse=True))
for w in sorted_dict:
    print('%s\t%s' % ( w , sorted_dict[w] )) 