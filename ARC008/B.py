from math import ceil
from collections import defaultdict
d1 = defaultdict(int)
d2 = defaultdict(int)

n, m = map(int, input().split())
s = input()
t = input()

for i in range(n):
    d1[ord(s[i]) - 65] += 1
for i in range(m):
    d2[ord(t[i]) - 65] += 1

ans = 0
for i in range(26):
    if d1[i] == 0:
        continue
    if d1[i] > 0 and d2[i] == 0:
        print(-1)
        exit()
    if d1[i] > 0:
        ans = max(ceil(d1[i] / d2[i]), ans)
print(ans)
