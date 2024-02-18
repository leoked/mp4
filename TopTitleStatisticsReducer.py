#!/usr/bin/env python3
import sys
import math

numbers = []
for line in sys.stdin:
    n = int(line.strip())
    numbers.append(n)

Sum = sum(numbers)
Mean = math.floor(Sum / len(numbers))
Min = min(numbers)
Max = max(numbers)
Var = math.floor(sum((xi - Mean) ** 2 for xi in numbers) / len(numbers))

print('Mean\t%s' % ( Mean ))
print('Sum\t%s' % ( Sum ))
print('Min\t%s' % ( Min ))
print('Max\t%s' % ( Max ))
print('Var\t%s' % ( Var ))