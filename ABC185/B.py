N, M, T = map(int, input().split())
AB = list(list(map(int, input().split())) for _ in range(M))
total = N
for i in range(M):
    a = AB[i][0]
    b = AB[i][1]
    if i == 0:
        total -= AB[i][0]
    else:
        total -= AB[i][0] - AB[i-1][1]
    if total <= 0:
        print('No')
        exit()
    total += AB[i][1] - AB[i][0]
    total = min(total, N)
total -= T - AB[-1][1]
if total <= 0:
    print('No')
    exit()
print('Yes')
