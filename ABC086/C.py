n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i == 0:
        diff_t = txy[i][0]
        diff_ab = abs(txy[i][1]) + abs(txy[i][2])
    else:
        diff_t = txy[i][0] - txy[i-1][0]
        diff_ab = abs(txy[i][1] - txy[i-1][1]) + abs(txy[i][2]-txy[i-1][2])
    # 距離判定
    if diff_ab > diff_t:
        print('No')
        exit()
    # 奇数偶数判定
    if diff_ab % 2 != diff_t % 2:
        print('No')
        exit()
print('Yes')
