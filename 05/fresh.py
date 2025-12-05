#!/bin/env python3

import fileinput

with fileinput.input() as f:
    rr1 = []
    for line in f:
        if line == '\n': break
        rr1.append(tuple(int(a) for a in line.split('-')))
    ii = [int(a) for a in f]

rr1.sort()
rr = [rr1[0]]
for r in rr1[1:]:
    if rr[-1][1] < r[0]: rr.append(r)
    elif rr[-1][1] <= r[1]: rr[-1] = (rr[-1][0], r[1])

# Step 1
count = 0
for i in ii:
    for r in rr:
        if r[0] <= i <= r[1]:
            count += 1
            break

print(f"============\n{count}")

# Step 2
count = 0
for r in rr:
    count += 1 + r[1] - r[0]

print(f"{count}")
