def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N, P = map(int, input().split())
a = prime_factorize(P)
b = set(a)
ans = 1
for x in b:
    cnt = a.count(x)
    if cnt >= N:
        ans *= x**(cnt // N)
print(ans)
