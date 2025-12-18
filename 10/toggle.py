#!/bin/env python3

import fileinput

def toggle(d, n, nn):
    global depth
    if n == 0:
        depth = d
    elif nn and d<depth:
        toggle(d, n, nn[1:])
        toggle(d+1, n^nn[0], nn[1:])

tot = 0
for line in fileinput.input():
    mm = [tuple(el[1:-1].split(',')) for el in line.strip().split()]
    depth = len(mm[0][0])-1
    ts = sum(1 << (depth-int(b)) for b,c in enumerate(mm[0][0]) if c=='#')
    bb = [sum(1 << (depth-int(b)) for b in a) for a in mm[1:-1]]
    toggle(0, ts, bb)
    tot += depth
print(tot)
