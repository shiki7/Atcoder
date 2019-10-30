import collections
import itertools

n = int(input())
s = [input()[0] for _ in range(n)]
counter = collections.Counter(s)
ans = 0
for a, b, c in itertools.combinations('MARCH', 3):
    ans += counter[a] * counter[b] * counter[c]
print(ans)
