from collections import defaultdict
d = defaultdict(int)

H, W = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(H))

for i in range(H):
    for j in range(W):
        d[a[i][j]] += 1
min_d = min(d.keys())
ans = 0
for k, v in d.items():
    if k > min_d:
        ans += (k-min_d)*v
print(ans)
