#!/bin/env python3

import fileinput
import math

def divs(n):
    if n<2: return
    yield 1
    for i in range(2, 1+int(math.sqrt(n))):
        if n%i == 0:
            yield i
            if n//i != i:
                yield n//i

s = 0
rr = [tuple(n for n in r.split('-')) for r in next(fileinput.input()).strip().split(',')]
for r1,r2 in rr:
    pp = [(r1[:n], len(r1)//n) for n in divs(len(r1))]
    if len(r2) > len(r1):
        pp.extend(("1"+"0"*(n-1), len(r2)//n) for n in divs(len(r2)))
    n1,n2 = int(r1),int(r2)
    m = set()
    for p, n in pp:
        while int(p*n) <= n2:
            pn = int(p*n)
            if pn >= n1 and pn not in m:
                m.add(pn)
                s += pn
            p = str(int(p)+1)

print(s)
