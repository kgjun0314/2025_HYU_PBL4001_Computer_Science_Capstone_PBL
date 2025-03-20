import sys
import bisect

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    m = list(map(int, read().split()))
    answer = 0
    m.sort()
    while len(m) != 0:
        limit = 900
        while len(m) != 0:
            idx = bisect.bisect_right(m, limit)
            if idx != 0:
                idx -= 1
                limit -= m[idx]
                del m[idx]
            else:
                answer += 1
                break
        if len(m) == 0:
            answer += 1
    print(answer)