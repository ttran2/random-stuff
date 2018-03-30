#!/usr/bin/python

import sys
from optparse import OptionParser

#---------- Arguments ----------

parser=OptionParser()
parser.add_option("-d","--detail",action="store_true",dest="detail",help="print out debug messages")
parser.add_option("-c","--color",action="store_true",dest="color",help="print out messages and boards with colors")
parser.add_option("-s","--solve",action="store_true",dest="solve",help="solve the sudoku puzzle")
(opt,args)=parser.parse_args()


#---------- CONSTANTS ----------

#errors
ERR_ROW_NUM = 101
ERR_COL_NUM = 102
ERR_NUM = 103

#incorrect
INCOR_ROW = 201
INCOR_COL = 202
INCOR_BOX = 203

#other
SOLVED = 1
CORRECT = 0

#-------------------------------

MSG = {
    ERR_ROW_NUM:"incorrect number of row",
    ERR_COL_NUM:"incorrect number of column",
    ERR_NUM:"an incorrect number detected",

    INCOR_ROW:"repeated number in a row",
    INCOR_COL:"repeated number in a column",
    INCOR_BOX:"repeated number in a small box",

    SOLVED:"the game is already solved",
    CORRECT:"the board follows sudoku rules",
}

#-------------------------------

def state(constant):
    if constant >= 200:
        return "incorrect"
    elif constant >= 100:
        return "error"
    elif constant == 1:
        return "solved"
    else:
        return "correct"

"""
def dPrint(string,alternative=None):
    if __debug__:
        #stdout.write(s)
        print string
    elif alternative:
        print alternative
"""

def dPrint(string,alternative=None):
    if opt.detail:
        print string
        alternative = None
    if alternative:
        print alternative

class Game:
    def __init__(self):
        self.board = []

    def load(self):
        for line in sys.stdin:
            if line.strip() == "":
                continue
            self.board.append([int(n) for n in line.split()])

    def verify(self):
        #check number of row
        if len(self.board) != 9:
            return ERR_ROW_NUM #return "error","incorrect number of row"

        #check number of column
        for row in self.board:
            if len(row) != 9:
                return ERR_COL_NUM #return "error","incorrect number of column"

        #check if number are from 0 - 9
        for row in self.board:
            for number in row:
                if number not in range(10): #number < 0 or number > 9:
                    return ERR_NUM #return "error","an incorrect number detected"

        #check unique number
        if self.checkUnique(self.board): #check in row
            return INCOR_ROW #return "incorrect","repeated number in a row"

        if self.checkUnique(self.getColumns()): #check in column
            return INCOR_COL #return "incorrect","repeated number in a column"

        if self.checkUnique(self.getBox()): #check in box
            return INCOR_BOX #return "incorrect","repeated number in a small box"

        if self.checkSolved():
            return SOLVED #return "solved","the game is already solved"
        else:
            return CORRECT #return "correct",""

    def checkSolved(self):
        #check if any 'empty spots' (zeros)
        for i in xrange(9):
            if len(self.removeZero(self.board)[i]) != len(self.board[i]):
                return False #there is zero therefore its not solved
        return True #board is solved

    def checkUnique(self,list): #True = not unique, none = unique
        list = self.removeZero(list)
        for part in list:
            if len(part) != len(set(part)):
                return True

    def getColumns(self):
        columnList = []
        for columnN in xrange(9): #looping column
            column = []
            for i in xrange(9): #looping row
                column.append(self.board[i][columnN])
            columnList.append(column)
        return columnList

    def getBox(self): #spent around 1 hour creating this -_-
        boxlist = []
        for Ysection in xrange(0,9,3): #[0,3,6]
            for Xsection in xrange(0,9,3): #[0,3,6]
                box = []
                for rowN in xrange(3): #[0,1,2]
                    box.extend(self.board[rowN + Ysection][Xsection:Xsection+3])
                boxlist.append(box)
        return boxlist

    def removeZero(self,list):
        removed = []
        for part in list:
            removed.append(filter(lambda n: n != 0, part))
        return removed

    def boxNumber(self,rowN,columnN):
        #data = [[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[0,0,0,1,1,1,2,2,2],[3,3,3,4,4,4,5,5,5],[3,3,3,4,4,4,5,5,5],[3,3,3,4,4,4,5,5,5],[6,6,6,7,7,7,8,8,8],[6,6,6,7,7,7,8,8,8],[6,6,6,7,7,7,8,8,8]]
        #boxN = data[rowN][columnN]
        #return boxN
        return (columnN/3 + rowN - (rowN % 3))

    def genPossibilities(self):
        list = []
        rowN = 0
        for row in self.board:
            newRow = []
            columnN = 0
            for tile in row:
                if tile == 0:
                    possibleNum = self.calculatePossible(rowN,columnN)
                else:
                    possibleNum = []
                newRow.append(possibleNum)
                columnN = columnN + 1
            list.append(newRow)
            rowN = rowN + 1
        self.possibilities = list

    def calculatePossible(self,rowN,columnN):
        possibleNum = [1,2,3,4,5,6,7,8,9]
        row = self.board[rowN]
        column = self.getColumns()[columnN] #can be more efficient
        box = self.getBox()[self.boxNumber(rowN,columnN)]

        for list in row, column, box:
            for number in list:
                if number in possibleNum:
                    possibleNum.remove(number)
        return possibleNum

    def solvingLoop(self):
        while True:
            self.genPossibilities()
            tilesFilled = self.onePossible() #number of tiles that had one possible number
            if tilesFilled == 0:
                if not self.checkSolved():
                    dPrint("Sorry, this puzzle is out of my ability :-(")
                    return False
                else:
                    dPrint("Mission accomplished! :-D")
                    return True

    def onePossible(self):
        possBoard = self.possibilities
        successNumber = 0
        rowN = 0
        for row in possBoard:
            columnN = 0
            for tile in row:
                if len(tile) == 1:
                    self.insert(tile[0],rowN,columnN) #tile number, row number, column number
                    successNumber = successNumber + 1
                columnN = columnN + 1
            rowN = rowN + 1
        dPrint("I found " + str(successNumber) + " tile(s) that have one possible number.")
        return successNumber

    def insert(self,value,rowN,columnN):
        self.board[rowN][columnN] = value

    def boardPrint(self):
        rowN = 0
        for row in self.board:
            if rowN == 3:
                print ""
                rowN = 0
            columnN = 0
            for tile in row:
                if columnN == 3:
                    print "",
                    columnN = 0
                print str(tile),
                columnN = columnN + 1
            print ""
            rowN = rowN + 1

if __name__ == "__main__":
    #color()
    g = Game()
    try:
        g.load()
        #dPrint("BOARD DATA:\n" + str(g.board) + "\n" + "-"*30)
    except ValueError:
        dPrint("[ ERROR ] Invalid character detected","error")
        raise SystemExit
    except:
        dPrint("[ ERROR ] Unknown error","error")
        raise SystemExit

    g.boardPrint()
    print "" #new line to seperate received board and message

    verifyResult = g.verify()
    dPrint("[" + state(verifyResult).upper() + "] " + MSG[verifyResult].capitalize(), state(verifyResult))
    #if verifyResult[0] != "correct":
    if verifyResult:
        #dPrint("[ " + verifyResult[0].upper() + " ] " + verifyResult[1].capitalize(), verifyResult[0])
        raise SystemExit

    #dPrint("[SUCCESS] The board follows sudoku rules","correct")

    if not opt.solve: #check for 'solve' argument
        raise SystemExit

    solve = g.solvingLoop()
    print "" #new line to seperate message and solved board
    g.boardPrint()
    if solve:
        print "solved" #for the test suite
