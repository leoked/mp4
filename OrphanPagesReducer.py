#!/usr/bin/env python3
import sys

fList = []
tList = []

for line in sys.stdin:
  line = line.strip().split('\t')
  fList.append(int(line[0].strip()))
  tp = line[1].split(' ')
  for p in tp:
    if p == line[0].strip():
      continue
    tList.append(int(p.strip()))

fList = set(fList)
tList = set(tList)

oList = fList.difference(tList)
oList = sorted(oList)

for i in oList:
  print(i)