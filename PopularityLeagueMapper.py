#!/usr/bin/env python3
import sys

leaguePath = sys.argv[1]

with open(leaguePath) as f:
       league = f.read().split('\n')

print(league)
for line in sys.stdin:
       line = line.strip().split('\t')
       if line[0] in league:
              print('%s\t%s' % ( line[0] , line[1] ))
