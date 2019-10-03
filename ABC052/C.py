import math


# 素因数分解（試し割り法）
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


n = int(input())
fact = prime_factorize(math.factorial(n))
before_x = 1
total = 1
count = 0
for i in range(len(fact)):
    if fact[i] == before_x:
        count += 1
    else:
        total *= (count + 1)
        count = 1
        before_x = fact[i]
    if i == len(fact) - 1:
        if fact[i] == before_x:
            total *= (count + 1)
        else:
            total *= 2
print(total % ((10**9) + 7))
