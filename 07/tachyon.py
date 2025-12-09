#!/bin/env python3

import fileinput

mm = [line.strip() for line in fileinput.input()]
ss = [0] * len(mm[0])
ss[mm[0].index('S')] = 1

count = 0
for m in mm[2:]:
    for i,c in enumerate(m):
        if c=='^':
            ss[i-1] += ss[i]
            ss[i+1] += ss[i]
            if ss[i]: count += 1
            ss[i] = 0

print(f"============\n{count}", sum(ss))
