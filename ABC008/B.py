import collections

n = int(input())
s = [input() for _ in range(n)]
max_s = max(s)
c = collections.Counter(s)
print(c.most_common()[0][0])
