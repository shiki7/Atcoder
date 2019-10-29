n, m = map(int, input().split())

if m == 2 * n:
    print(n)
elif m > 2 * n:
    print(n + (m - 2 * n) // 4)
elif m < 2 * n:
    print(m // 2)
