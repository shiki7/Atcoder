n, m = map(int, input().split())


def nCr(n, r, mod=10**9+7):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


if n >= 2 and m >= 2:
    print(nCr(n, 2) + nCr(m, 2))
elif n >= 2 and m <= 1:
    print(nCr(n, 2))
elif n <= 1 and m >= 2:
    print(nCr(m, 2))
else:
    print(0)
