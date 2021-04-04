x, y = map(int, input().split())
if y % 2 != 0:
    print(-1)
    exit()
a = y // 2
if -a <= x <= a and x % 2 == a % 2:
    print(a)
else:
    print(-1)
