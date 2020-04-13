n, a, b = map(int, input().split())
if a > b:
    print(0)
elif n == 1:
    if a != b:
        print(0)
    else:
        print(1)
else:
    print((a+b+b*(n-2)) - (a+b+a*(n-2)) + 1)
