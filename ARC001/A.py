from collections import defaultdict
n = int(input())
s = input()

dd = defaultdict(int)
for i in range(1, 5):
    dd[i] = 0
for i in range(n):
    dd[int(s[i])] += 1
print(max(dd.values()), min(dd.values()))
