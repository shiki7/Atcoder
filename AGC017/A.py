n, p = map(int, input().split())
a = list(map(int, input().split()))
dp0 = [1]*(n+1)
dp1 = [0]*(n+1)
for i in range(n):
    if a[i] % 2 == 0:
        dp0[i+1] = dp0[i]+dp0[i]
        dp1[i+1] = dp1[i]+dp1[i]
    else:
        dp0[i+1] = dp0[i]+dp1[i]
        dp1[i+1] = dp0[i]+dp1[i]
if p % 2 == 0:
    print(dp0[-1])
else:
    print(dp1[-1])
