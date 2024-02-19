#!/usr/bin/env python3

import sys
import string
import json

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopWords = f.read().split('\n')

with open(delimitersPath) as f:
    delimiter = f.read()

for line in sys.stdin:
    data = json.loads(line)
    bid = data['business_id']
    star = int(data['stars']) - 3
    text = str(data['text']).lower()
    for c in delimiter:
        if c == ' ':
            continue
        text = text.replace(c, '')
    text = text.split(' ')
    wCount = 0
    for w in text:
        if w in stopWords:
            continue
        wCount += 1

    score = star * wCount
    print('%s\t%s' % ( bid , score ))
