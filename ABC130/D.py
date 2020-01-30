import bisect
import itertools
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 累積和
b = [0] + list(itertools.accumulate(a))

# 2分探索
# n+1 - 累積和bへの(left+k)の挿入index を足し合わせて求める
ans = 0
for i in range(n):
    ans += n+1 - bisect.bisect_left(b, b[i]+k)
print(ans)
