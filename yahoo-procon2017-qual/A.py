from collections import defaultdict
d = defaultdict(int)
s = input()

for i in range(5):
    d[s[i]] += 1
if d["y"] == 1 and d["a"] == 1 and d["h"] == 1 and d["o"] == 2:
    print('YES')
else:
    print('NO')
