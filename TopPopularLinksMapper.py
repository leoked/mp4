#!/usr/bin/env python3
import sys

count = 0
for line in sys.stdin:
        if count < 10:
                line = line.strip().split('\t')
                print('%s\t%s' % ( line[0] , line[1]))
                count += 1