import sys
read = sys.stdin.readline

offer = []
N = int(read())
for i in range(N):
    line = list(map(int, read().split()))
    Ai = line[0]  # i번째 소비자가 한 제안 수
    for j in range(Ai):
        Sij = line[2 * j + 1]  # 신차 크기 조건
        Pij = line[2 * j + 2]  # 소비자가 지불하겠다는 가격
        offer.append([Sij, Pij, i + 1])  # [크기조건, 가격, 소비자 번호] 저장

Q = []
M = int(read())
line = list(map(int, read().split()))
for i in range(M):
    Q.append([line[i], i + 1]) # [매출 목표, 시나리오 인덱스] 저장

offer.sort()
Q.sort()

revenue = 0 # 현재까지 가능한 최대 매출
max_p = [0] * (N + 1) # 각 소비자별 가장 많이 낼 수 있는 제안 금액
qIdx = 0 # 시나리오 인덱스
for i in range(len(offer)):
    s = offer[i][0] # 차량 크기 조건
    p = offer[i][1] # 지불 가격
    buyer = offer[i][2] # 소비자 번호
    
    if max_p[buyer] < p:
        revenue += p - max_p[buyer] # 최대 p 갱신하기 전에 차이만큼 수익 증가
        max_p[buyer] = p
        while qIdx < M and Q[qIdx][0] <= revenue: # 수익이 qIdx번 째 신차의 매출 목표를 넘는다면
            Q[qIdx].append(s) # qIdx번 째 신차의 최소 크기는 s
            qIdx += 1
            
# 아직 결과가 안 채워진 시나리오들은 만족 불가 (-1)
while qIdx < M:
    Q[qIdx].append(-1)
    qIdx += 1
# 원래 순서대로 출력하기 위해 시나리오 인덱스 기준으로 정렬
Q.sort(key = lambda x : x[1])
for i in range(M):
    print(Q[i][2], end = " ")