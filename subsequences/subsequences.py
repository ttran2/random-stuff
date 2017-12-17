#!/usr/bin/python
import sys

v = sys.stdin.read().split()
short = min(v,key=len)
v.remove(short)
short = list(short)
tmp = ""
best = ""
i = 0
while i < len(short):
    tmp = tmp + short[i]
    for l in v: #loop other words
#DEV        print "testing: " + tmp,
        if tmp not in l:
            if len(tmp) != 1:
#DEV                print "Nope"
                i = i - len(tmp) + 1
                tmp = ""
            else:
                tmp = ""
            break
#DEV        print "yey!"
    if len(tmp) > len(best):
        best = tmp
    i = i + 1
print best