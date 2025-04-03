import sys
read = sys.stdin.readline

N, M, K = map(int, read().split())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)] # dp[i][j] = (A[i-1] == B[j-1])인 상태의 A[0:i]와 B[0:j]의 가장 긴 연속 공통 부분의 길이

result = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])

print(result)