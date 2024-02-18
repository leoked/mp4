#!/usr/bin/env python3
import sys

count = 0
countList = []
# input comes from STDIN
for line in sys.stdin:
    if count == 10:
        break

    line = line.strip()
    countList.append(line)
    count += 1

for item in reversed(countList):
    print(item)