#!/bin/env python3

import fileinput
from math import sqrt

def dist(p1, p2):
    return sqrt(abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2+abs(p1[2]-p2[2])**2)
    
mm = [tuple(int(n) for n in line.strip().split(',')) for line in fileinput.input()]
pp = [(dist(p1,p2),p1,p2) for i,p1 in enumerate(mm[:-1]) for p2 in mm[i+1:]]
pp.sort()

# Part 1
cc = []
for d,p1,p2 in pp[:1000]:
    n = {p1, p2}
    for c in cc.copy():
        if c >= n: break
        if c & n:
            n |= c
            cc.remove(c)
    else:
        cc.append(n)

nn = sorted((len(c) for c in cc), reverse=True)
tot = nn[0]*nn[1]*nn[2]

# Part 2
cc = []
fin = None
for d,p1,p2 in pp:
    n = {p1, p2}
    for c in cc.copy():
        if c >= n: break
        if c & n:
            fin = p1[0]*p2[0]
            n |= c
            cc.remove(c)
    else:
        cc.append(n)

print(f"============\n{tot}", fin)
