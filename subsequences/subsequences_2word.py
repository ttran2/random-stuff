#!/usr/bin/python
import sys
n
v = sys.stdin.read().split()
short, long = v[:2] #take only first two words, randomly assigned variable

if len(long) < len(short):
    short,long = long,short

tmp = ""
best = ""
for i in list(short):
    tmp = tmp + i
    if tmp in long:
        if len(tmp) > len(best):
            best = tmp
    else:
        tmp = ""

print best
