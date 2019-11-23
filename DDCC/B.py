n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
total = 0
min_diff = 10**10
min_idx = 0
total_tmp = 0
for i in range(n):
    total += a[i]
    diff = abs(total - sum_a/2)
    if diff < min_diff:
        min_diff = diff
        min_idx = i
        total_tmp = total

print(abs(total_tmp - sum(a[min_idx+1:])))
