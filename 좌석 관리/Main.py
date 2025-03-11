import sys
read = sys.stdin.readline
import math

N, M, Q = map(int, read().split(" "))
seats = [[0 for j in range(M + 1)] for i in range(N + 1)]
ate = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def allSeatsEmpty():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if seats[i][j] != 0:
                return False
    return True

def findById(id):
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if seats[i][j] == id:
                return (i, j, True)
    return (-1, -1, False)

def leaveFromSeat(x, y):
    ate.append(seats[x][y])
    seats[x][y] = 0

def valid(x, y):
    return (1 <= x and x <= N and 1 <= y and y <= M)

def adjEmpty(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(valid(nx, ny)):
            if(seats[nx][ny] != 0):
                return False
    return True

def calcD(X, Y):
    D = 987654321
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if seats[i][j] != 0:
                D = min(D, math.sqrt((i - X) ** 2 + (j - Y) ** 2))
    return D

def getSeat():
    D = -1
    x = -1
    y = -1
    flag = False
    for X in range(1, N + 1):
        for Y in range(1, M + 1):
            if seats[X][Y] == 0 and adjEmpty(X, Y) == True:
                newD = calcD(X, Y)
                if newD != 987654321 and D < newD:
                    flag = True
                    D = newD
                    x = X
                    y = Y
    return (x, y, flag)
    
for _ in range(Q):
    cmd, id = read().split(" ")
    id = int(id)
    if cmd == "In":
        x, y, flag = findById(id)
        if flag == True:
            print("{0} already seated.".format(id))
        elif id in ate:
            print("{0} already ate lunch.".format(id))
        elif allSeatsEmpty() == True:
            seats[1][1] = id
            print("{0} gets the seat ({1}, {2}).".format(id, 1, 1))
        else:
            x, y, flag = getSeat()
            if flag == False:
                print("There are no more seats.")
            else:
                seats[x][y] = id
                print("{0} gets the seat ({1}, {2}).".format(id, x, y))
    elif cmd == "Out":
        if id in ate:
            print("{0} already left seat.".format(id))
        else:
            x, y, flag = findById(id)
            if flag == False:
                print("{0} didn't eat lunch.".format(id))
            else:
                leaveFromSeat(x, y)
                print("{0} leaves from the seat ({1}, {2}).".format(id, x, y))