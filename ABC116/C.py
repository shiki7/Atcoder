N = int(input())
h = list(map(int, input().split()))

cur = 0
total = 0
while h != [0] * N:
    for i in range(cur, N):
        if cur == i and h[i] == 0:
            cur += 1
        elif h[i] == 0:
            if cur == i - 1:
                total += h[i - 1]
                h[i - 1] = 0
            else:
                min_h = min(h[cur:i])
                total += min_h
                for j in range(cur, i):
                    h[j] -= min_h
        elif i == N - 1:
            min_h = min(h[cur:N])
            total += min_h
            for j in range(cur, N):
                h[j] -= min_h
print(total)
