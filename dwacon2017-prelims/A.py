n, a, b = map(int, input().split())
if a+b <= n:
    print(0)
else:
    print(a+b-n)
