#!/bin/env python3

import fileinput
from collections import Counter


pp = {li[:3]: li.split()[1:] for li in fileinput.input()}|{'out': []}


def paths(start, end, count=1):
    vis = Counter({end: 0})
    s0 = Counter({start: count})
    while s0:
        s1 = Counter()
        for s,v in s0.items():
            for n in pp[s]:
                s1[n] += v
                vis[n] += v
        s0 = s1
    return vis[end]


p1 = paths('you', 'out')
print("first ", p1)

p1 = paths('svr', 'fft')
p2 = paths('fft', 'dac', p1)
p3 = paths('dac', 'out', p2)
print("second", p3)
