N, M = map(int, input().split())
a = 0
for i in range(1, N+1):
    a += i**2
print(a % M)
