N = int(input())
a = list(map(int, input().split()))

b = 0
for i in range(N):
    b = b ^ a[i]

ans = []
for i in range(N):
    ans.append(b ^ a[i])
print(*ans)
