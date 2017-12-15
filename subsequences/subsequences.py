#!/usr/bin/python
import sys

v = sys.stdin.read().split()
short = min(v,key=len)
v.remove(short)
tmp = ""
best = ""
for i in list(short): #loop char of shortest word
    tmp = tmp + i
    for l in v: #loop other words
        if tmp not in l:
            tmp = ""
            break
    if len(tmp) > len(best):
        best = tmp
print best