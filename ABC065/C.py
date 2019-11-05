from math import factorial

n, m = map(int, input().split())
if abs(n-m) > 1:
    print(0)
    exit()
if n == m:
    print(2 * factorial(n) * factorial(m) % (10**9+7))
else:
    print(factorial(n) * factorial(m) % (10**9+7))
