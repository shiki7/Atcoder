from math import factorial

x, y = map(int, input().split())

if (x + y) % 3 != 0:
    print(0)
    exit()
if x > 2*y or y > 2 * x:
    print(0)
    exit()


if x == y:
    print(factorial((x*2//3)) // (factorial(x//3) ** 2) % (10**9+7))
else:
    n = (x + y) // 3
    r = abs(x-y)//3
    print(factorial(n) //
          (factorial(r) * factorial(n-r)) % (10**9+7))
