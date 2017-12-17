#!/usr/bin/python
from random import randint, choice
from colorama import init, Fore, Style

def convert(n):
    if n == 0:
        return "green"
    elif n in range(1,11) + range (19,29):
        if n % 2 == 0:
            return "black"
        else:
            return "red"
    else:
        if n % 2 == 0:
            return "red"
        else:
            return "black"

#constant
startingBudget = 100
players = 5
maxRounds = 10
baseBet = 10
analysis = True
interactive = True
color = True

#color
if color:
    init()
    cDefault = Fore.WHITE
    cTitle = Fore.YELLOW
    cSignificant = Fore.RED
    cSubtitle = Fore.CYAN
    cName = Fore.GREEN
    cError = Fore.RED + "[!] "
    cSignificant2 = Fore.MAGENTA
else:
    cDefault = ""
    cTitle = ""
    cSignificant = ""
    cSubtitle = ""
    cName = ""
    cError = "[!] "
    cSignificant2 = ""

#create a history
h = [randint(0,36) for a in range(maxRounds)]

data = []

#for data2 collection
if interactive:
    data2 = [[]]*players

#main loop
print Style.BRIGHT + cDefault + "Starting simulation..."
for p in range(players): #player num is p+1
    winRate = 0
    highestM = [0,0,0,0] #most money in an instant| round, money, winrate, winRow
    winRow = 0 #wins in a row now
    winRowH = [0,0] # win in a row highest| round, highest win in row
    comeback = 0 # barely escaped
    r = 0
    b = baseBet
    m = startingBudget
    for n in h: #n-winning num
        if b == 0:
            break
        r = r + 1
        m = m - b
        c = choice(["red", "black"])
        #print "ROUND " + str(r) + " | money: " + str(m) + " | bet: " + str(b),
        lb = b #save bet for data2
        if c == convert(n): #win
            #print " | WIN"
            winRow = winRow + 1
            if winRow > winRowH[1]:
                winRowH = [r,winRow]
            winRate = winRate + 1
            m = m + b * 2
            b = baseBet
            if m > highestM[1]:
                highestM = [r,m,winRate,winRow]
        else:
            #print " | LOSE"
            winRow = 0
            b = b * 2
            if b >= m:
                b = m#all in
                comeback = comeback + 1
        if interactive:
            if winRow == 0:
                winL = "LOSE"
            else:
                winL = "WIN"
#ERROR            data2[p].append([r,winL,lb,m]) #[round n, winning row, betted, balance], [...], ... <lb> is betted coins ALSO the location of data is the player name e.g. data2[0] is player 1
    data.append([p+1,r,m,winRate,highestM,winRowH,comeback])

#ANALYZE
print cDefault +  "Starting analyzing...\n"
print cTitle + "-"*80
print cSubtitle + "Number of players: " + cSignificant + str(players)
print cSubtitle + "Player's budget: " + cSignificant + str(startingBudget) + cDefault + " coins"
print cSubtitle + "Maximum amount of rounds: " + cSignificant + str(maxRounds)
print cSubtitle + "Player's base bet: " + cSignificant + str(baseBet)
print cTitle + "-"*80
print ""

#how many and who did/didn't bancrupt + survival rate
survivor = []
for i in data:
    if i[2] != 0:
        survivor.append([str(i[0]), str(i[2])])
ls = len(survivor)
if ls == 0:
    print cDefault + "All of the " + cSignificant + str(players) + cDefault + " players went bancrupt!"
else:
    if ls == 1:
        print cDefault + "There is " + cSignificant + "one single player" + cSignificant + " that didn't go bancrupt:"
    else:
        print cDefault + "There are " + cSignificant + str(ls) + cDefault + " players that didn't go bancrupt:"
    for name in survivor:
        print cName + "Player " + name[0] + cDefault + " still has " + cSignificant + str(name[1]) + cDefault + " coins."
    print cDefault + "The survival rate is " + cSignificant + str(float(float(ls)/players)*100) + "%"
print ""

#if constant anlysis is false then finish
if not analysis:
    exit()

#lowest and highest round and average
if ls == 0:
    rh = [0,0]
else:
    rh = ["x",maxRounds+1]
rl = [0,maxRounds]
instLost = []
rv = 0
for i in data:
    if i[1] == 4:
        instLost.append(str(i[0]))
    elif i[1] > rh[1]:
        rh = [i[0],i[1]]
    elif i[1] < rl[1]:
        rl = [i[0],i[1]]
    else:
        pass
    rv = rv + i[1]
print cDefault + "The average number of rounds are " + cSignificant + str(float(rv)/players) + cDefault + "."
inst = len(instLost)
if inst == 0:
    print cName + "Player " + str(rl[0]) + cDefault + " bancrupted the fastest, just in " + cSignificant + str(rl[1]) + cDefault + " rounds."
elif inst <= 6:
    print cName + "Player " + ", ".join(instLost) + cDefault + " bancrupted instantly without winning a single round"
    print cDefault + "which means that " + cSignificant + str(round(float(inst)/players,2)*100) + "%" + cDefault + " of the players have a " + cSignificant + "0%" + cDefault + " success rate!"
else:
    print cDefault + "There are " + cSignificant + str(inst) + cDefault + " players that bancrupted instantly without winning a single round"
    print cDefault + "which means that " + cSignificant + str(round(float(inst)/players,2)*100) + "%" + cDefault + " of the players have a " + cSignificant + "0%" + cDefault + " success rate!"
if rh[0] != "x":
    print cName + "Player " + str(rh[0]) + cDefault + " bancrupted as the last, in round number " + cSignificant + str(rh[1]) + cDefault + "."
print ""

#win ammount and success rate
winH = [0,0]
winL = [0,maxRounds+1]
wv = 0
raH = [0,0]
raL = [0,101]
rav = 0
for i in data:
    if i[3] > winH[1]:
        winH = [i[0],i[3],i[1]]
    elif i[3] < winL[1]:
        winL = [i[0],i[3],i[1]]
    else:
        pass
    rate = float(float(i[3])/i[1])*100
    if rate > raH[1]:
        raH = [i[0],rate]
    elif rate < raL[1]:
        raL = [i[0],rate]
    else:
        pass
    rav = rav + rate
    wv = wv + i[3]
print cName + "Player " + str(winH[0]) + cDefault + " won the most bets with " + cSignificant + str(winH[1]) + cDefault + " wins (and " + cSignificant + str(winH[2]-winH[1]) + cDefault + " lost)."
if inst == 0:
    print cName + "Player " + str(winL[0]) + cDefault + " won the least bets with " + cSignificant + str(winL[1]) + cDefault + " wins (and " + cSignificant + str(winL[2]-winL[1]) + cDefault + " lost)."
print cDefault + "The average number of bets won per player is " + cSignificant + str(float(wv)/players) + cDefault + "."
print cDefault + "The most successful player is " + cName + "Player " + str(raH[0]) + cDefault + " with " + cSignificant + str(round(raH[1],2)) + "%" + cDefault + " success rate in betting."
if inst == 0:
    print cDefault + "The least successful player is " + cName + "Player " + str(raL[0]) + cDefault + " with " + cSignificant + str(round(raL[1],2)) + "%" + cDefault + " success rate in betting."
print cDefault + "The players average success rate is " + cSignificant + str(float(rav)/players) + "%" + cDefault + "."
print ""

#highest coin in possesion
cH = [0,0,0,0,0]#player,round,money,winrate,winrow
ac = 0
for i in data:
    if i[4][1] > cH[1]:
        cH = [i[0]] + i[4]
    ac = ac + i[4][1]
print cName + "Player " + str(cH[0]) + cDefault + " had the highest amount of coins in his possesion at one point."
print cDefault + "The player had " + cSignificant + str(cH[2]) + cDefault + " coins at round number " + cSignificant + str(cH[1]) + cDefault + "."
print cDefault + "Prior the point, the player had " + cSignificant + str(round(float(cH[3])/cH[1],4)*100) + "%" + cDefault + " success rate in betting (" + cSignificant + str(cH[3]) + cDefault + " bets won)."
print cDefault + "Before reaching the point, the player had " + cSignificant + str(cH[4]) + cDefault + " consecutive wins."
print cDefault + "The average highest amount in possesion per player is " + cSignificant + str(float(ac)/players) + cDefault + " coins."
print ""

#winning streak
st = [0,0,0]
stv = 0
for i in data:
    if i[5][1] > st[1]:
        st = [i[0],i[5][1],i[5][0]]
    stv = stv + i[5][1]
print cName + "Player " + str(st[0]) + cDefault + " has the longest winning streak (in round number " + cSignificant + str(st[2]) + cDefault + ")."
print cDefault + "The player had " + cSignificant + str(st[1]) + cDefault + " consecutive wins."
print cDefault + "The average highest winning streak per player is " + cSignificant + str(float(stv)/players) + cDefault + " consecutive wins."
print ""

#comeback
cb = [0,0]
cbv = 0
for i in data:
    if i[6] > cb[1]:
        cb = [i[0],i[6]]
    cbv = cbv + i[6]
print cName + "Player " + str(cb[0]) + cDefault + " is the most persistent player  since he/she went all-in " + cSignificant + str(cb[1])  + cDefault + " times."
print cDefault + "The average amount of going all-in is " + cSignificant + str(float(cbv)/players) + cDefault + " times per player."

#data interactive
while interactive:
    print cTitle + "-"*80
    print cDefault + "Search data: <" + cName + "PLAYER NUMBER" + cDefault + "> <" + cSignificant + "ROUND RANGE" + cDefault + ">"
    print cDefault + "Special commands: " + cSubtitle + "(h)elp, (hi)story,(q)uit"
    cmd = raw_input(cTitle + "Command: " + cSubtitle).lower().split()
    if len(cmd) == 0:
        print cError + "No command nor argument registered!"
        print cError + "type 'help' for a help message"
    elif cmd[0] == "h" or cmd[0] == "help":
        print cTitle + "-"*35 + " [ HELP ] " + "-"*35
        print cDefault + "Get data (player): [" + cSignificant + "PLAYER NUMBER" + cDefault + "] [" + cSignificant + "ROUND RANGE" + cDefault + "]"
        print cDefault + "Get data (round): [" + cSignificant + "ROUND NUMBER" + cDefault + "]"
        print cDefault + "Special commands: " + cSignificant + "(h)elp, (hi)story,(q)uit"
        print cDefault + "Example: 149 58-78 - this search for " + cName + "Player 149" + cDefault + " data on rounds between round " + cSignificant + "58" + cDefault + " and " + cSignificant + "78" + cDefault + "."
        print cSignificant2 + "\tPLAYER NUMBER" + cDefault + " - expected input is a number"
        print cSignificant2 + "\tROUND RANGE" + cDefault + " - expected values: two number seperated by a dash or 'x' (all rounds)"
        print cSignificant2 + "\tROUND NUMBER" + cDefault + " - expected a single number"
        print cSubtitle + "\tHelp" + cDefault + " - show this message"
        print cSubtitle + "\tHistory" + cDefault + " - show roulette games history"
        print cDefault + "\t\texcepted argument: [" + cSignificant2 + "ROUND RANGE" + cDefault + "] or 'x'"
        print cSubtitle + "\tQuit" + cDefault + " - quit this program"
    elif cmd[0] == "hi" or cmd[0] == "history":
        print cTitle + "-"*26 + " [ ROULETTE GAMES HISTORY ] " + "-"*26
        try:
            if cmd[1] == "x":
                fromR, toR = 1, maxRounds
            else:
                fromR,toR = cmd[1].split("-")
                fromR, toR = int(fromR), int(toR)
        except:
            print cError + "Invalid argument."
            print cError + "Expected argument is [ROUND RANGE] or 'x'"
            print cError + "type 'help' for more information"
            continue
        r = 0
        for n in h:
            r = r +1
            if fromR > r or toR < r:
                continue
            cn = convert(n)
            if color:
                if cn == "red":
                    cRoulette = Fore.RED
                elif cn == "black":
                    cRoulette = Fore.WHITE
                else:
                    cRoulette = Fore.GREEN
            else:
                cRoulette = ""
            print cSubtitle  + "\t" + str(r) + ". " + cRoulette + str(n) + " (" + cn + ")\t"
    elif cmd[0] == "quit" or cmd[0] == "q" or cmd[0] == "exit" or cmd[0] == "e":
        quit()
    elif len(cmd) == 1:
        print cTitle + "-"*29 + " [ DATA FOR A ROUND ] " + "-"*29
        try:
            r = int(cmd[0])
        except:
            print cError + "Not recognized command!"
            print cError + "type 'help' for more information"
            continue
        if not 1 <= r <= maxRounds:
            print cError + "Invalid round number!"
            print cError + "Round number have to be between 1 and " + str(maxRounds)
            continue
        print cError + "This function is in development!"
        print cError + "The function recognize that you want data for round number " + str(r)
        #for l in data2:
    else:
        print cTitle + "-"*28 + " [ DATA FOR PLAYER(S) ] " + "-"*28
        if len(cmd) != 2:
            print cError + "Invalid number of argument (2 expected, " + str(len(cmd)) + " given)"
            print cError + "type 'help' for more information"
        try:
            playerN = int(cmd[0])
            if cmd[1] == "x":
                fromR, toR = 1, maxRounds
            else:
                fromR,toR = cmd[1].split("-")
                fromR, toR = int(fromR), int(toR)
        except:
            print cError + "Invalid argument."
            print cError + "Expected argument is [ROUND RANGE] or 'x'"
            print cError + "type 'help' for more information"
            continue
        print cError + "This function is in development!"
        print cError + "The function know that you want data from Player " + str(playerN)
        print cError + "and that you want to collect data only from round " + str(fromR) + " to round " + str(toR)
        #for i in xrange(fromR,toR+1):
        #    print data2[playerN-1][i-1]