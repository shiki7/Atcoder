def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b


n, m = map(int, input().split())
if m == 0:
    print(fib(n) % 1000000007)
    exit()
a = [int(input()) for _ in range(m)]

total = 1
i = 0
for x in a:
    if x == i:
        print(0)
        exit()
    total *= fib(x - i - 1)
    i = x + 1
if a[-1] != n:
    total *= fib(n - (a[-1] + 1))

print(total % 1000000007)
