#!/usr/bin/python

#from difflib import *
from math import sqrt

def gap(dataList):
    x = []
    """
    # gaps between items that are next to each other
    for item_1, item_2 in zip(b[:-1], b[1:]): # [ ( item1 , item1+1), ( item2 , item2+1),... ]
        x.append(abs(item_2 - item_1))
    """
    # all gaps between item which are not necessary next to each other
    for item_1 in dataList:
        for item_2 in dataList:
            x.append(abs(item_2 - item_1))
    return sum(x)/len(x)

def compare(targetNumber, dataList):
    x = []
    for value in dataList:
        #x.append(abs(value - targetNumber))
        x.append(abs(howSimilar(targetNumber, value)))

    """
    #----- check outliers
    for i in x:
        if gap(x)
    #-----
    """

    print "-"*20
    return sum(x)/len(x)

def howSimilar(value_1, value_2):
    # https://stackoverflow.com/questions/26109959/get-the-similarity-of-two-numbers-with-python
    if value_1 > value_2:
        value_1, value_2 = value_2, value_1

    a = value_1 * value_1
    b = value_2 * value_2

    x = a / sqrt(a * b)
    print x
    return x

a = 12
b = [12,5,12,3,12,3]
c = [5,5,5,5,5,5,5,5,5,5,5,100000]
d = [5,5,5,5,5,5,5]
print "<<< TESTING >>>"
print "a: %s" % a
print "b: %s" % b
print "c: %s" % c
print "d: %s" % d