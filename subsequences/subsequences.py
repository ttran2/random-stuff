#!/usr/bin/python -O
from sys import stdin,stdout

def dPrint(s):
    if __debug__:
        stdout.write(s)
        #stdout.flush()

v = stdin.read().split()
short = min(v,key=len)
v.remove(short)
short = list(short)
tmp = ""
best = ""
i = 0
while i < len(short):
    tmp = tmp + short[i]
    for l in v: #loop other words
        dPrint("testing: " + tmp + "\t\t")
        if tmp not in l:
            dPrint("Nope!\n")
            if len(tmp) != 1:
                i = i - len(tmp) + 1
                tmp = ""
            else:
                tmp = ""
            break
        dPrint("Yey!\n")
    if len(tmp) > len(best):
        dPrint("Best: " + tmp + "\n")
        best = tmp
    i = i + 1
print best