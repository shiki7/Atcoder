def nCr(n, r, mod=10**9+7):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


x, y = map(int, input().split())

if (x + y) % 3 != 0:
    print(0)
    exit()
if x > 2*y or y > 2 * x:
    print(0)
    exit()

# 以下の連立方程式を解いて、代入
# n + 2m  = X
# 2n+ m = Y
# (n+m)Cn
print(nCr((x + y)//3, (-x+2*y)//3))
