#!/usr/bin/python
import sys

n = int(sys.argv[1])
for i in xrange(2, n / 2 + 1):
    if n % i == 0:
        print str(i),
