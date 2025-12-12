#!/bin/env python3

import fileinput

def area(p1, p2):
    return (1+p2[0]-p1[0])*(1+p2[1]-p1[1])

mm = [tuple(int(n) for n in line.strip().split(',')) for line in fileinput.input()]

# All possible squares sorted by area
pp = (((min(x1,x2),min(y1,y2)),(max(x1,x2),max(y1,y2))) for i,(x1,y1) in enumerate(mm[:-1]) for (x2,y2) in mm[i+1:])
pp = sorted(((area(p1,p2),p1,p2) for p1,p2 in pp), reverse=True)

a1 = pp[0][0]
print("Part 1 =", a1)

# Only consider vertical lines
ll = ((mm[i],mm[(i+1)%len(mm)]) for i in range(len(mm)))
ll = sorted(((x1,min(y1,y2)),(x2,max(y1,y2))) for ((x1,y1),(x2,y2)) in ll if x1 == x2)

for a,p1,p2 in pp:
    # Lines intersecting inside square
    if any(True for (x,y1),(_,y2) in ll if p1[0] < x < p2[0] and y1 < p2[1] and y2 > p1[1]):
        continue
    # Count line segments to the left of square
    ii = sorted((y1,y2) for (x,y1),(_,y2) in ll if x <= p1[0] and y1 <= p2[1] and y2 >= p1[1])
    # Gaps above or below
    if not ii or ii[0][0] > p1[1] or ii[-1][1] < p2[1]:
        continue
    # Even number inside list
    c = 1
    i1 = ii[0]
    for i in ii[1:]:
        if i[0] != i1[0] and c&1 == 0: break
        if i[0] < i1[1]: c += 1
        elif i[0] > i1[1]: c -= 1
        i1 = i
    if c&1:
        print("Part 2 =", a)
        break
