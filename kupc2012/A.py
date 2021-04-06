N, T, E = map(int, input().split())
x = list(map(int, input().split()))
for i in range(T-E, T+E+1):
    for j in range(N):
        if i % x[j] == 0:
            print(j+1)
            exit()
print(-1)
