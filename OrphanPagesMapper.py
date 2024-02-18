#!/usr/bin/env python3
import sys

for line in sys.stdin:
  line.strip().split(':')
  fp = line[0].strip()
  tp = line[1].strip().split(' ')
  for p in tp:
    if tp == fp:
      continue
    print('%s\t%s' % ( fp , tp ))
