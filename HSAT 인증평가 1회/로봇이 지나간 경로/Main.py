import sys
from collections import deque

read = sys.stdin.readline

H, W = map(int, read().split())
grid = [list(read().rstrip()) for _ in range(H)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def valid(y, x):
    return 0 <= y < H and 0 <= x < W

def bfs(y, x, d):
    ret = ""
    visited = [[False] * W for _ in range(H)]

    queue = deque()
    ny, nx = y + dy[d], x + dx[d]
    nny, nnx = ny + dy[d], nx + dx[d]

    visited[y][x] = True
    visited[ny][nx] = True
    visited[nny][nnx] = True
    queue.append((nny, nnx, d))

    ret += "A"

    while queue:
        cur_y, cur_x, cur_d = queue.popleft()

        for nd in range(4):
            next_y, next_x = cur_y + dy[nd], cur_x + dx[nd]
            next2_y, next2_x = next_y + dy[nd], next_x + dx[nd]

            if not (valid(next_y, next_x) and valid(next2_y, next2_x)):
                continue
            if not (grid[next_y][next_x] == '#' and grid[next2_y][next2_x] == '#'):
                continue
            if visited[next_y][next_x] or visited[next2_y][next2_x]:
                continue

            if nd == cur_d:
                ret += "A"
            elif (cur_d + 1) % 4 == nd:
                ret += "LA"
            elif (cur_d - 1) % 4 == nd:
                ret += "RA"

            visited[next_y][next_x] = True
            visited[next2_y][next2_x] = True
            queue.append((next2_y, next2_x, nd))

    return ret

startPoint = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            sharpCnt = 0
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if valid(ny, nx) and grid[ny][nx] == '#':
                    sharpCnt += 1
            if sharpCnt == 1:
                startPoint.append((i, j))

answerY = 0
answerX = 0
answerD = 0
answerCommandLen = 987654321
answerCommand = ""

for i, j in startPoint:
    for d in range(4):
        ny, nx = i + dy[d], j + dx[d]
        nny, nnx = ny + dy[d], nx + dx[d]
        if valid(ny, nx) and valid(nny, nnx):
            if grid[ny][nx] == '#' and grid[nny][nnx] == '#':
                command = bfs(i, j, d)
                if 0 < len(command) < answerCommandLen:
                    answerCommandLen = len(command)
                    answerCommand = command
                    answerY = i + 1
                    answerX = j + 1
                    answerD = d

print(answerY, answerX)
print(["^", "<", "v", ">"][answerD])
print(answerCommand)
