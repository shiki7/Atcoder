import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


a, b = map(int, input().split())
c = gcd(a, b)
d = factorize(c)
print(len(set(d))+1)
