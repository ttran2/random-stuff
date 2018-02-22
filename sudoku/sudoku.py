#!/usr/bin/python

import sys

def dPrint(s):
    if __debug__:
        #stdout.write(s)
        print s

class Game:
    def __init__(self):
        self.board = []

    def load(self):
        for line in sys.stdin:
            self.board.append([int(n) for n in line.split()])

    def verify(self):
        #check number of row
        if len(self.board) != 9:
            return

        #check number of column
        for row in self.board:
            if len(row) != 9:
                return

        #check if number are from 0 - 9
        for row in self.board:
            for number in row:
                if number < 0 or number > 9: #if number in xrange(0,10):
                    return

        #check unique number
        noZero = self.removeZero()

        #---check in row
        for row in noZero:
            if len(row) != len(set(row)):
                return

        #---check in column
        #rowN = 0
        #while rowN < 9:
        #    print noZero[rowN]
        #    rowN = rowN + 1

        return True

    def removeZero(self):
        list = []
        for row in self.board:
            list.append(filter(lambda n: n != 0, row))
        return list


if __name__ == "__main__":
    g = Game()
    try:
        g.load()
    except:
        print "NO"
        raise SystemExit
    if not g.verify():
        print "NO"
        raise SystemExit
    print "YES"
    print g.board