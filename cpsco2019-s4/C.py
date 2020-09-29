from bisect import bisect_right

N, D = map(int, input().split())
R = list(map(int, input().split()))
R = sorted(R)
cnt = 0
# 始点を固定して２分探索
for i in range(N-2):
    idx = bisect_right(R, R[i]+D)-1
    cnt += (idx - i) * (idx - i - 1) // 2
print(cnt)
