from collections import defaultdict
d1 = defaultdict(int)
d2 = defaultdict(int)

L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

for i in range(L):
    d1[l[i]] += 1
for i in range(R):
    d2[r[i]] += 1

ans = 0
for x in d1:
    if d2[x]:
        ans += min(d1[x], d2[x])
print(ans)
