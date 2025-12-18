#!/bin/env python3

import fileinput
from collections import defaultdict

# 1. Make all numbers even -> reuse solution 1 to toggle low bits off!
# 2. Divide by two
# 3. Repeat 1 or 2 depending on if uneven nbrs exist

def toggle(n0, n, nn, ln, d=0, vv=[]):
    global tog
    if n == 0:
        tog[n0].add((d, tuple(sum((v>>i)&1 for v in vv) for i in range(ln, -1, -1))))
    if nn:
        toggle(n0, n, nn[1:], ln, d, vv)
        toggle(n0, n^nn[0], nn[1:], ln, d+1, vv+[nn[0]])


def result(bb, cc):
    global tog, res
    if cc in res: return res[cc]
    ts = sum(1 << (n-int(b)) for b,c in enumerate(cc) if c&1)
    if ts not in tog: toggle(ts, ts, bb, len(cc)-1)
    press = 1000000
    for d,vv in tog[ts]:
        cc1 = tuple(a-b for a,b in zip(cc, vv))
        if all(c >= 0 for c in cc1):
            cc1 = tuple(a//2 for a in cc1)
            press = min(press, d + 2*result(bb, cc1))
    res[cc] = press
    return press


tot = 0
for line in fileinput.input():
    #print(line.strip())
    mm = [tuple(el[1:-1].split(',')) for el in line.strip().split()]
    n = len(mm[-1])-1
    bb = [sum(1 << (n-int(b)) for b in a) for a in mm[1:-1]]
    cc = tuple(int(c) for c in mm[-1])
    res = {tuple(0 for _ in cc): 0}
    tog = defaultdict(set)
    r = result(bb, cc)
    tot += r
    print(r)

print(f"=========\n{tot}")
