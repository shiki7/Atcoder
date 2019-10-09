import collections

n = int(input())
a = list(map(int, input().split()))
counter = collections.Counter(a)
ans = 0
for k, v in counter.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v - k
print(ans)
