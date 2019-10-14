import collections
n = int(input())
a = list(map(int, input().split()))

counter = collections.Counter(a)
ans = 1
for k, v in counter.items():
    if k != 0:
        if v == 2:
            ans *= 2
        if v == 1:
            ans = 0
            break
print(ans % (10**9 + 7))
