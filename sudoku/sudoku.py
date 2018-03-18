#!/usr/bin/python

import sys

"""
def dPrint(string,alternative=None):
    if __debug__:
        #stdout.write(s)
        print string
    elif alternative:
        print alternative
"""

def dPrint(string,alternative=None):
    try:
        if sys.argv[1] in ["-d","--details","details"]:
            print string
            alternative = None
    except IndexError:
        pass
    if alternative:
        print alternative

"""
def color():
    try:
        global cDefault, cColor
        if sys.argv[1] in ["-c","--color","--colors","color","colors"]:
            from colorama import init, Fore
            init()
            cDefault = Fore.WHITE
            cColor = Fore.RED
        else:
            print "NO COLOR"
            cDefault = cColor = ""
    except IndexError:
        pass
"""

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
            return "error","incorrect number of row"

        #check number of column
        for row in self.board:
            if len(row) != 9:
                return "error","incorrect number of column"

        #check if number are from 0 - 9
        for row in self.board:
            for number in row:
                if number not in range(10): #number < 0 or number > 9:
                    return "error","an incorrect number detected"

        #check unique number
        if self.checkUnique(self.board): #check in row
            return "incorrect","repeated number in a row"

        if self.checkUnique(self.getColumns()): #check in column
            return "incorrect","repeated number in a column"

        if self.checkUnique(self.getBox()): #check in box
            return "incorrect","repeated number in a small box"

        if self.checkSolved():
            return "solved","the game is already solved"
        else:
            return "correct",""

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

    def boxNumber(self,rowN,columnN): #UGLY SOLUTION! need to be rewrited!
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
        dPrint("BOARD DATA:\n" + str(g.board) + "\n" + "-"*30)
    except ValueError:
        dPrint("[ ERROR ] Invalid character detected","error")
        raise SystemExit
    except:
        dPrint("[ ERROR ] Unknown error","error")
        raise SystemExit

    verifyResult = g.verify()
    if verifyResult[0] != "correct":
        dPrint("[ " + verifyResult[0].upper() + " ] " + verifyResult[1].capitalize(), verifyResult[0])
        raise SystemExit

    #start solving it...
    dPrint("[SUCCESS] The board follows sudoku rules","correct")
    if g.solvingLoop():
        g.boardPrint()
    else:
        dPrint("\n" + "-"*30 + "BOARD DATA:\n" + str(g.board) + "\n" + "-"*30)