#!/usr/bin/python
import sys

#n=range(2,int(sys.argv[1]))
#for i in n:
#    print str(i)
#    for a in n:
#        if a%i==0:
#            n.remove(a)
try:
    n=int(sys.argv[1])
except:
    exit()
l=set()
for i in xrange(2,n+1):
#    print "i am at: "+str(i)
    if i not in l:
        print i,
        l.add(i)
        for a in xrange(i*i,n+1,i):
            l.add(a)
