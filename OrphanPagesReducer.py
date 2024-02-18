#!/usr/bin/env python3
import sys

fList = []
tList = []

for line in sys.stdin:
  line = line.strip().split('\t')
  
  fList.append(int(line[0].strip()))
  tList.append(int(line[1].strip()))

fList = set(fList)
tList = set(tList)

oList = fList.difference(tList)
oList = sorted(oList)

for i in oList:
  print(i)