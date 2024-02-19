#!/usr/bin/env python3
from operator import itemgetter
import sys

yelp = dict()

# input comes from STDIN
for line in sys.stdin:
    line = line.strip().split('\t')
    
    if line[0] in yelp:
        yelp[line[0]][0] += int(line[1])
        yelp[line[0]][1] += 1
    else:
        yelp[line[0]] = [int(line[1]),1]

yelpTotal = []
for item in yelp:
    rate = yelp[item][0] / yelp[item][1]
    yelpTotal.append([item, rate])

yelpTotal = sorted(yelpTotal,key=lambda x : x[1], reverse=True)

for item in yelpTotal:
    print('%s\t%s' % ( item[0] , int(item[1]) ))
