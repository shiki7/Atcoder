from bisect import bisect_left

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = sorted(b)
count = 0
for i in range(na):
    idx = bisect_left(b, a[i])
    if idx >= nb:
        continue
    if b[idx] == a[i]:
        count += 1
print(count/(na+nb-count))
