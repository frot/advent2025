#!/bin/env python3

import fileinput
import operator
from functools import reduce

mm = [line.strip('\n') for line in fileinput.input()]
ops = mm.pop()
s = 0
nn = []
for i,op in reversed(list(enumerate(ops))):
    n = "".join(m[i] for m in mm if m[i]!=' ')
    if n: nn.append(int(n))
    if op=='+': fn = operator.add
    elif op=='*': fn = operator.mul
    else: continue
    print(op, reduce(fn, nn))
    s += reduce(fn, nn)
    nn = []

print(f"============\n{s}")
