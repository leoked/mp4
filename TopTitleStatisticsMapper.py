#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip().split('\t')
    
    print('%s' % ( line[1] ))
