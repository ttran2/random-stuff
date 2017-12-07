#!/usr/bin/python
from random import randint, choice

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
players = 1000
maxRounds = 2000
baseBet = 10

#create a history
h = [randint(0,36) for a in range(maxRounds)]

data = []

#main loop
print "Starting simulation..."
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
    data.append([p+1,r,m,winRate,highestM,winRowH,comeback])

#ANALYZE
print "Starting analyzing...\n"
print "-"*80
print "Number of players: " + str(players)
print "Player's budget: " + str(startingBudget) + " coins"
print "Maximum amount of rounds: " + str(maxRounds)
print "Player's base bet: " + str(baseBet)
print "-"*80
print ""

#how many and who did/didn't bancrupt + survival rate
survivor = []
for i in data:
    if i[2] != 0:
        survivor.append([str(i[0]), str(i[2])])
ls = len(survivor)
if ls == 0:
    print "All of the " + str(players) + " players went bancrupt!"
else:
    if ls == 1:
        print "There is one single player that didn't go bancrupt:"
    else:
        print "There are " + str(ls) + " players that didn't go bancrupt:"
    for name in survivor:
        print "Player " + name[0] + " still has " + str(name[1]) + " coins."
    print "The survival rate is " + str(float(float(ls)/players)*100) + "%"
print ""

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
print "The average number of rounds are " + str(float(rv)/players) + "."
inst = len(instLost)
if inst == 0:
    print "Player " + str(rl[0]) + " bancrupted the fastest, just in " + str(rl[1]) + " round."
elif inst <= 6:
    print "Player " + ", ".join(instLost) + " bancrupted instantly without winning a single round"
    print "which means that " + str(round(float(inst)/players,2)*100) + "% of the players have a 0% success rate!"
else:
    print "There are " + str(inst) + " players that bancrupted instantly without winning a single round"
    print "which means that " + str(round(float(inst)/players,2)*100) + "% of the players have a 0% success rate!"
if rh[0] != "x":
    print "Player " + str(rh[0]) + " bancrupted as the last, in round number " + str(rh[1]) + "."
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
print "Player " + str(winH[0]) + " won the most bets with " + str(winH[1]) + " wins (and " + str(winH[2]-winH[1]) + " lost)."
if inst == 0:
    print "Player " + str(winL[0]) + " won the least bets with " + str(winL[1]) + " wins (and " + str(winL[2]-winL[1]) + " lost)."
print "The average number of bets won per player is " + str(float(wv)/players) + "."
print "The most successful player is Player " + str(raH[0]) + " with " + str(round(raH[1],2)) + "% success rate in betting."
if inst == 0:
    print "The least successful player is Player " + str(raL[0]) + " with " + str(round(raL[1],2)) + "% success rate in betting."
print "The players average success rate is " + str(float(rav)/players) + "%."
print ""

#highest coin in possesion
cH = [0,0,0,0,0]#player,round,money,winrate,winrow
ac = 0
for i in data:
    if i[4][1] > cH[1]:
        cH = [i[0]] + i[4]
    ac = ac + i[4][1]
print "Player " + str(cH[0]) + " had the highest amount of coins in his possesion at one point."
print "The player had " + str(cH[2]) + " coins at round number " + str(cH[1]) + "."
print "Prior the point, the player had " + str(round(float(cH[3])/cH[1],4)*100) + "% success rate in betting (" + str(cH[3]) + " bets won)."
print "Before reaching the point, the player had " + str(cH[4]) + " consecutive wins."
print "The average highest amount in possesion per player is " + str(float(ac)/players) + " coins."
print ""

#winning streak
st = [0,0,0]
stv = 0
for i in data:
    if i[5][1] > st[1]:
        st = [i[0],i[5][1],i[5][0]]
    stv = stv + i[5][1]
print "Player " + str(st[0]) + " has the longest winning streak (in round number " + str(st[2]) + ")."
print "The player had " + str(st[1]) + " consecutive wins."
print "The average highest winning streak per player is " + str(float(stv)/players) + " consecutive wins."
print ""

#comeback
cb = [0,0]
cbv = 0
for i in data:
    if i[6] > cb[1]:
        cb = [i[0],i[6]]
    cbv = cbv + i[6]
print "Player " + str(cb[0]) + " is the most persistent player  since he/she went all-in " + str(cb[1])  + " times."
print "The average amount of going all-in is " + str(float(cbv)/players) + " times per player."