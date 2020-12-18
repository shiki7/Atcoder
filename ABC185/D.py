from math import ceil

N, M = map(int, input().split())
a = [0] + list(map(int, input().split())) + [N+1]
if N == M:
    print(0)
    exit()

a = sorted(a)
diff = []
min_diff = float('inf')
for i in range(1, M+2):
    tmp = a[i] - a[i-1] - 1
    if tmp > 0:
        diff.append(tmp)
        min_diff = min(min_diff, tmp)

if min_diff == 1:
    print(N-M)
    exit()

ans = 0
for i in range(len(diff)):
    ans += ceil(diff[i] / min_diff)
print(ans)
