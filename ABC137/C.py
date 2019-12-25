from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

d = defaultdict(int)
for i in range(n):
    d["".join(sorted(s[i]))] += 1

ans = 0
for k in d.keys():
    ans += d[k] * (d[k]-1) // 2
print(ans)
