#!/usr/bin/python
import sys

for a in sys.argv[1:]:
    try:
        n=int(a)
    except:
        continue
    if n<2:
        print a+" is NOT a prime"
        continue
    #for i in range(2,int(n**0.5)+1): #all numbers between 2 and n^0.5+1
    for i in range(2,int(n**0.5)):
    #for i in range(2,n/2):
        if n%i==0:#divide n / i and return zbytek
            print a+" is NOT a prime"
            break
    else:
        print a+" is a prime"
