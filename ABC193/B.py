N = int(input())
ans = float('inf')
flg = False
for i in range(N):
    A, P, X = map(int, input().split())
    if A < X:
        ans = min(ans, P)
        flg = True
if flg:
    print(ans)
else:
    print(-1)
