n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    min_dis = float("inf")
    min_idx = 0
    for j in range(m):
        dis = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if dis < min_dis:
            min_dis = dis
            min_idx = j
    print(min_idx + 1)
