import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

image = []
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def valid(i, j):
    if 0 <= i < H and 0 <= j < W:
        return True
    else:
        return False

def dfs(i, j, c, color):
    image[i][j] = c
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if valid(ni, nj) and image[ni][nj] == color:
            dfs(ni, nj, c, color)

H, W = map(int, read().split())
for _ in range(H):
    row = list(map(int, read().split()))
    image.append(row)    
    
Q = int(read())
for _ in range(Q):
    i, j, c = map(int, read().split())
    i -= 1
    j -= 1
    color = image[i][j]
    if color != c:
        dfs(i, j, c, color)

for i in range(H):
    for j in range(W):
        print(image[i][j], end = " ")
    print()