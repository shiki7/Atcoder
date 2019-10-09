import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))

counter = collections.Counter(a)
counter_sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
ans = n
for i in range(min(k, len(counter_sorted))):
    ans -= counter_sorted[i][1]
print(ans)
