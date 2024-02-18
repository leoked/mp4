#!/usr/bin/env python3
import sys

fList = set()
tList = set()

for line in sys.stdin:
  line = line.strip().split('\t')
  fList.add(int(line[0].strip()))
  tList.add(int(line[1].strip()))

oList = list(fList.difference(tList))
oList = sorted(oList)

for i in oList:
  print(i)