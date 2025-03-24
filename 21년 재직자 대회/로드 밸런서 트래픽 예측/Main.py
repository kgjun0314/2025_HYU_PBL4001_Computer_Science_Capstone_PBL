import sys
from collections import deque
sys.setrecursionlimit(10**9)
read = sys.stdin.readline

def calculate_indegree(graph):
    indegree = [0] * (len(graph))
    for i in range(1, len(graph)):
        for next in graph[i]:
            indegree[next] += 1
    return indegree

def topological_sort(graph):
    result = []
    indegree = calculate_indegree(graph)
    queue = deque([])
    for i in range(1, len(graph)):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        result.append(cur)
        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)            
    return result

N, K = map(int, read().split())
r = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, read().split()))
    r[i] = line[0]
    line.pop(0)
    for e in line:
        graph[i].append(e)

topology = topological_sort(graph)
traffic = [0] * (N + 1)
traffic[1] = K
for i in range(N):
    cur_node = topology[i]
    request = traffic[cur_node]
    if r[cur_node] == 0:
        continue
    quotient = request // r[cur_node]
    remainder = request % r[cur_node]
    for j in range(r[cur_node]):
        next_node = graph[cur_node][j]
        traffic[next_node] += quotient
    for j in range(remainder):
        next_node = graph[cur_node][j]
        traffic[next_node] += 1

print(*traffic[1:])