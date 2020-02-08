n, x = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) == x:
    print(n)
elif sum(a) < x:
    print(n-1)
else:
    a = sorted(a)
    total = 0
    for i in range(n):
        total += a[i]
        if total == x:
            print(i+1)
            exit()
        elif total > x:
            print(i)
            exit()
