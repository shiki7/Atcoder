from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
    d[b[c[i]-1]] += 1

ans = 0
for i in range(N):
    ans += d[a[i]]
print(ans)
