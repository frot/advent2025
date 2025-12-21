#!/bin/env python3

import fileinput

s = 0
pp = {}
for line in fileinput.input():
    p = line.strip().split()
    pp[p[0][:-1]] = p[1:]

qq = pp['you'].copy()

while qq:
    q = qq.pop()
    if q == 'out': s += 1
    else: qq.extend(pp[q])

print(f"============\n{s}")
