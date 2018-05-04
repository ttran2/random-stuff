#!/usr/bin/python

#from difflib import *
from sys import stdin
#from math import sqrt

def input():
    list = []
    #list = stdin.read().split()
    for item in stdin:
        if item == "\n":
            continue
        list.append(float(item))
    number = list.pop(0)
    return number, list

def gapInList(dataList):
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

def gapTargetNumber(targetNumber, dataList):
    x = []
    for item_1 in dataList:
        x.append(abs(targetNumber - item_1))
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

    #print "-"*20
    return sum(x)/len(x)

def howSimilar(value_1, value_2):
    # https://stackoverflow.com/questions/26109959/get-the-similarity-of-two-numbers-with-python

    if value_1 > value_2:
        value_1, value_2 = value_2, value_1

    """
    a = value_1 * value_1
    b = value_2 * value_2

    x = a / sqrt(a * b)
    """

    x = abs(float(value_1)/float(value_2))

    #print x
    return x

if __name__ == "__main__":
    number, list = input()
    print "Targeted number: %s" % number
    print "There is a similarity of: %s %%" % (compare(number,list)*100)
    print "-"*30
    x = gapTargetNumber(number,list)
    print "Average gap between targeted number and list: %s" % x
    y = gapInList(list)
    print "Average gap between item in list: %s" % y
    print "The gaps similarity is: %s %%" % (howSimilar(x,y)*100)
