#!/bin/env python3

import fileinput
from pprint import pprint

rr = [["."] + [c for c in r.strip()] + ["."] for r in fileinput.input()]
rr = [["."]*len(rr[0])] + rr + [["."]*len(rr[0])]

count = 0
c1 = 0
while True:
    rr2 = rr.copy()
    for row,r in enumerate(rr):
        for col,c in enumerate(r):
            if c == '@':
                n = (rr[row-1][col-1:col+2].count('@') +
                     rr[row][col-1:col+2].count('@') +
                     rr[row+1][col-1:col+2].count('@'))
                if n < 5:
                    count += 1
                    rr2[row][col] = '.'
    # break  # Step 1
    if count == c1: break;  # Step 2
    c1 = count
    rr = rr2

print(f"============\n{count}")
