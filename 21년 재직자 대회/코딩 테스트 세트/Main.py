import sys
read = sys.stdin.readline

def test(c, d, x, N):
    tempc = c[:]
    tempd = d[:]
    for i in range(N):
        if tempc[i] >= x:
            continue
        need = x - tempc[i]

        if i > 0:
            take = min(tempd[i - 1], need)
            tempc[i] += take
            tempd[i - 1] -= take
            need -= take

        if i < N - 1 and need > 0:
            take = min(tempd[i], need)
            tempc[i] += take
            tempd[i] -= take
            need -= take

        if need > 0:
            return False
    
    return True

N, T = map(int, read().split())
for _ in range(T):
    scenario = list(map(int, read().split()))
    c = scenario[::2]
    d = scenario[1::2]
    answer = 0
    low = 0
    high = 2*10**12
    while low <= high:
        mid = (low + high) // 2
        if test(c, d, mid, N):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    print(answer)