from collections import defaultdict
s = input()
d = defaultdict(int)
for i in range(len(s)):
    d[s[i]] += 1
print(max(d, key=d.get))
