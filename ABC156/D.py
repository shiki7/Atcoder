n, a, b = map(int, input().split())
mod = 10**9 + 7


def nCr(n, r, mod):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


print((pow(2, n, mod)-1-nCr(n, a, mod)-nCr(n, b, mod)) % mod)
