#!/bin/env python3

import fileinput

s = 0
for line in fileinput.input():
    rr = [tuple(n for n in r.split('-')) for r in line.strip().split(',')]
    for r1,r2 in rr:
        if len(r1) & 1:
            p = "1" + "0"*(len(r1)//2)
        else:
            p = r1[:len(r1)//2]
        r1,r2 = int(r1),int(r2)
        while int(p+p) <= r2:
            if int(p+p) >= r1:
                s += int(p+p)
                print(p+p)
            p = str(int(p)+1)

print(f"============\n{s}")
