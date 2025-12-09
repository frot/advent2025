#!/bin/env python3

import fileinput
import operator
from functools import reduce

mm = [line.strip().split() for line in fileinput.input()]
ops = mm.pop()
s = 0
for i,op in enumerate(ops):
    if op=='+': fn = operator.add
    elif op=='*': fn = operator.mul
    s += reduce(fn, (int(m[i]) for m in mm))

print(f"============\n{s}")
