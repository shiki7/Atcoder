N, X = map(int, input().split())
L = list(map(int, input().split()))
d = 0
if L[0] > X:
    print(0)
for i in range(1, N + 1):
    d += L[i - 1]
    if d > X:
        print(i)
        exit()
print(N + 1)
