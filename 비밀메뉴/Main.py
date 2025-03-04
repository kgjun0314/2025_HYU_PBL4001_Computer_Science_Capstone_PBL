import sys
read = sys.stdin.readline

M, N, K = map(int, read().split(" "))
keyList = list(read().rstrip().split(" "))
sequenceList = list(read().rstrip().split(" "))

if M > N:
    print("normal")
    exit(0)

key = ""
for i in keyList:
    key += i

sequence = ""
for i in sequenceList:
    sequence += i

if key in sequence:
    print("secret")
else:
    print("normal")