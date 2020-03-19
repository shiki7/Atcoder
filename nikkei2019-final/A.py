# pypyじゃないと通らない
import itertools

N = int(input())
A = list(map(int, input().split()))

li = [0] + list(itertools.accumulate(A))
for i in range(1, N+1):
    ans = 0
    for j in range(N+1):
        ans = max(ans, li[j]-li[j-i])
    print(ans)
