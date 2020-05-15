N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

bad = set()
for i in range(M):
    if H[AB[i][0]-1] < H[AB[i][1]-1]:
        bad.add(AB[i][0])
    elif H[AB[i][0]-1] > H[AB[i][1]-1]:
        bad.add(AB[i][1])
    else:
        bad.add(AB[i][0])
        bad.add(AB[i][1])
print(N-len(bad))
