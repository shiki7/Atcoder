a, b = map(int, input().split())
if a > b:
    print(2 * a - 1)
elif a == b:
    print(a + b)
else:
    print(2 * b - 1)
