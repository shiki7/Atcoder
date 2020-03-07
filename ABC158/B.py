n, a, b = map(int, input().split())
c = n % (a+b)
d = n // (a+b)
if c <= a:
    print(d*a + c)
else:
    print((d+1)*a)
