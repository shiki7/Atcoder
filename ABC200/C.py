from collections import defaultdict
d = defaultdict(int)

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    d[A[i] % 200] += 1
ans = 0
for x, cnt in d.items():
    ans += cnt * (cnt - 1) // 2
print(ans)
