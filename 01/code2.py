#!/bin/env python3

import fileinput

n = 50
c = 0
for line in fileinput.input():
    n1 = n + int(line[1:]) if 'R' in line else n - int(line[1:])
    c += abs(n1)//100 + (n > 0 and n1 <= 0) or (n < 0 and n1 >= 0)
    n = n1 % 100
print(c)
