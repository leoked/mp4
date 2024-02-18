#!/usr/bin/env python3

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopWords = f.read().split('\n')

with open(delimitersPath) as f:
    delimiter = f.read().strip()

print(stopWords)
print(delimiter)

for line in sys.stdin:
    line = line.strip().lower()
    for c in delimiter:
        if c == '_':
            continue
        else:
            line = line.replace(c, '')
    words = line.split('_')
    for w in words:
        if w in stopWords:
            continue
        print('%s\t%s' % ( w , 1 )) 


