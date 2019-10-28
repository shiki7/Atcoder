import collections

n = int(input())
a = [int(input()) for _ in range(n)]

counter = collections.Counter(a)
ans = 0
for k, v in counter.items():
    if v % 2 != 0:
        ans += 1
print(ans)
