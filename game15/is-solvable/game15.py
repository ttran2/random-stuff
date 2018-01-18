#!/usr/bin/python

import sys
from miscellaneous import *

def dPrint(s):
    if __debug__:
        #stdout.write(s)
        print s

def reverse(target,max):
    return range(1, max+1)[-target]

class Game:
    def __init__(self,size=4):
        self.board = []
        self.size = size

    def load(self):
        #from STDIN create a board self.board
        for line in sys.stdin:
            self.board.append([int(n) for n in line.split()])

    def solve(self):
        pass

    def show(self):
        pass

    def verify(self):
        #check number of row
        if len(self.board) != self.size:
            return

        #check number of tiles in each row (aka check column)
        for row in self.board:
            if len(row) != self.size:
                return

        boardList = board2list(self.board)

        #check if all number are unique (not efficient but it is one-liner)
        if len(boardList) != len(set(boardList)):
            return

        #check if numbers are between 0 and ([boardSize]^2)-1 (since there is one empty "0" tile
        for n in boardList:
            if n > (self.size**2)-1 or n < 0:
                return

        #the math complicated verification
        inverted = self.inversion()
        dPrint("NUMBER OF INVERSION: " + str(inverted))
        if self.size %2 != 0: #if board size is odd
            if inverted %2 == 0: #and inverted is even, then it solvable
                return True
        else: #board size is even
            emptyTileRowReversed = reverse(self.whereEmpty()[0],self.size) #the row number of empty tile from bottom
            dPrint("BLANK is on (ROW x COLUMN): " + str(self.whereEmpty()))
            dPrint("Position of blank from the bottom: " + str(emptyTileRowReversed))
            if emptyTileRowReversed %2 != inverted %2:
                return True
            else:
                return

    def whereEmpty(self):
        #detects where "0" is, return (ROW , COLUMN)
        rowNumber = 1
        for row in self.board:
            columnNumber = 1
            for tile in row:
                if tile == 0:
                    return (rowNumber,columnNumber)
                columnNumber = columnNumber + 1
            rowNumber = rowNumber + 1

    def inversion(self):
        #behind X tile, count number smaller then X
        boardList = board2list(self.board)
        count = 0
        tileNumber = 0
        while tileNumber < len(boardList):
            for tile in boardList[tileNumber:]: #list of numbers after <boardList[tileNumber]>
                if boardList[tileNumber] > tile: #if the number after <boadList[tileNumber]> is bigger then number after it, count
                    if tile != 0: #tile 0 is empty and not a number so ignore it
                        count = count + 1
            tileNumber = tileNumber + 1
        return count

    def board2list(self):
        list = []
        for row in self.board:
            for tile in row:
                list.append(tile)
        return list

    def move(self,tile,targetPosition):
        pass


if __name__ == "__main__":
    g = Game()
    g.load()
    if not g.verify():
        print "NO"
        raise SystemExit
    print "YES"
    #print g.board
    #https://www.wikihow.com/Solve-a-15-Puzzle