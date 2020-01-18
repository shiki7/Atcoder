n, a, b = map(int, input().split())
c = n % (a+b)
if c <= a and c > 0:
    print('Ant')
else:
    print('Bug')
