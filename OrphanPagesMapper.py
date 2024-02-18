#!/usr/bin/env python3
import sys

for line in sys.stdin:
  line = line.strip().split(':')
  fp = line[0].strip()
  tp = line[1].strip()
  for p in tp:
    print('%s\t%s' % ( fp , tp ))
