import sys
read = sys.stdin.readline

N, M = map(int, read().split())
rooms = []
reservationInfo = {}
timeTable = {}

for _ in range(N):
    name = read().rstrip()
    rooms.append(name)
    timeTable[name] = [(i, i + 1) for i in range(9, 18)]
    reservationInfo[name] = [True] * 9

rooms.sort()
lastRoom = rooms[-1]

for _ in range(M):
    name, start, end = read().split()
    start = int(start)
    end = int(end)
    for i in range(start, end):
        for index, time in enumerate(timeTable[name]):
            if time[0] == i:
                reservationInfo[name][index] = False

for room in rooms:
    print("Room {0}:".format(room))
    if True not in reservationInfo[room]:
        print("Not available")
    else:
        flag = False
        cnt = 0
        for i in reservationInfo[room]:
            if i == True and flag == False:
                flag = True
                cnt += 1
            elif i == False:
                flag = False
        print("{0} available:".format(cnt))

        flag = False
        start = 0
        end = 0
        for index, info in enumerate(reservationInfo[room]):
            if info == True and flag == False:
                flag = True
                start = timeTable[room][index][0]
                end = timeTable[room][index][1]
                if end == 18:
                    if start == 9:
                        print("09", end="")
                    else:
                        print(start, end="")
                    print("-", end="")
                    print(end)
            elif info == True and flag == True:
                end = timeTable[room][index][1]
                if end == 18:
                    if start == 9:
                        print("09", end="")
                    else:
                        print(start, end="")
                    print("-", end="")
                    print(end)
            elif info == False and flag == True:
                if start == 9:
                    print("09", end="")
                else:
                    print(start, end="")
                print("-", end="")
                print(end)
                flag = False
    if room == lastRoom:
        break
    print("-----")