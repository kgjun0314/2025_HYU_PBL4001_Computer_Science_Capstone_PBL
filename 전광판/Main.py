import sys
read = sys.stdin.readline

numbers = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

T = int(read())

for _ in range(T):
    answer = 0
    A, B = read().rstrip().split(" ")
    while(len(A) != 5):
        A = '_' + A
    while(len(B) != 5):
        B = '_' + B
    for i in range(5):
        if A[i] == B[i]:
            continue
        else:
            if A[i] == '_':
                for j in numbers[int(B[i])]:
                    answer += j
            elif B[i] == '_':
                for j in numbers[int(A[i])]:
                    answer += j
            else:
                for j in range(7):
                    if numbers[int(A[i])][j] != numbers[int(B[i])][j]:
                        answer += 1
    print(answer)