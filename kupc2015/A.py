N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    t = S[i]
    cnt = 0
    while t:
        if t[:5] in ['tokyo', 'kyoto']:
            t = t[5:]
            cnt += 1
        else:
            t = t[1:]
    print(cnt)
