from collections import Counter
N = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
ans = 0
for k1, v1 in cnt.items():
    for k2, v2 in cnt.items():
        if k1 == k2:
            continue
        ans += (k1-k2)**2 * v1 * v2
print(ans//2)
