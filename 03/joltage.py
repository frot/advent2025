#!/bin/env python3

import fileinput

n = 12  # 2
s = 0
for bb in fileinput.input():
    i = 0
    b = [0]*n
    for x,y in enumerate(range(n, 0, -1)):
        i = 1+bb.index(max(bb[i:len(bb)-y]), i)
        b[x] = bb[i-1]
    s += int("".join(b))

print(f"============\n{s}")
