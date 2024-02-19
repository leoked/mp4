#!/usr/bin/env python3
import sys

league = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip().split('\t')

    league.append([int(line[0]) , int(line[1])])  

rank = [0] * len(league)

for i in range(len(league)):
    count = 0
    for j in range(len(league)):
        if league[i][1] > league[j][1]:
            count += 1
    rank[i] = count

for i in range(len(league)):
    league[i][1] = rank[i]

league = sorted(league, key=lambda x:x[0], reverse=True)

for item in league:
    print('%s\t%s' % ( item[0] , item[1] ))