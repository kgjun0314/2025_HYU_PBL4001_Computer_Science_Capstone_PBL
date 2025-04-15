import sys
from collections import deque
read = sys.stdin.readline

signal = [
    [],
    [1, 1, 1, 0, 3],
    [1, 1, 0, 1, 2],
    [1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 3],
    [1, 0, 0, 1, 2],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 3],
    [1, 1, 0, 0, 2],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0]
]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def valid(y, x):
    return 1 <= y <= N and 1 <= x <= N

def bfs(y, x, d, t):
    ret = 0
    queue = deque()
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    queue.append((y, x, d, t))
    visited[y][x] = True
    ret += 1
    while queue:
        cur_y, cur_x, cur_d, cur_t = queue.popleft()
        if cur_t == T:
            continue
        signal_set = signal_sets[cur_y][cur_x]
        signal_num = signal_set[cur_t % 4]
        sig = signal[signal_num]
        from_d = sig[4]
        if from_d != cur_d:
            continue
        for i in range(4):
            if sig[i] == 1:
                next_y = cur_y + dy[i]
                next_x = cur_x + dx[i]
                next_d = (i + 2) % 4
                next_t = cur_t + 1
                if valid(next_y, next_x):
                    queue.append((next_y, next_x, next_d, next_t))
                    if not visited[next_y][next_x]:
                        visited[next_y][next_x] = True
                        ret += 1
    return ret

N, T = map(int, read().split())
signal_sets = [[[] for i in range(N + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        signal_set = list(map(int, read().split()))
        signal_sets[i][j] = signal_set

result = bfs(1, 1, 2, 0)
print(result)