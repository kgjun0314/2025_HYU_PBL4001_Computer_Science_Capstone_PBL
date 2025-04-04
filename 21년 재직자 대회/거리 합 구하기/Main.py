import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

N = int(read())

tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    x, y, t = map(int, read().split())
    tree[x].append((y, t))
    tree[y].append((x, t))

subtree_size = [0] * (N + 1)
dist_sum = [0] * (N + 1)

def dfs1(cur_node, parent_node = 0):
    subtree_size[cur_node] = 1
    for next_node, next_weight in tree[cur_node]:
        if next_node != parent_node:
            dfs1(next_node, cur_node)
            subtree_size[cur_node] += subtree_size[next_node]
            dist_sum[cur_node] += next_weight * subtree_size[next_node] + dist_sum[next_node]

def dfs2(cur_node, parent_node = 0):
    for next_node, next_weight in tree[cur_node]:
        if next_node != parent_node:
            dist_sum[next_node] = dist_sum[cur_node] + next_weight * (N - 2 * subtree_size[next_node])
            dfs2(next_node, cur_node)

dfs1(1)
dfs2(1)

for i in range(1, N + 1):
    print(dist_sum[i])