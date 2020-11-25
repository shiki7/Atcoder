c1, r1 = map(int, input().split())
c2, r2 = map(int, input().split())
c = c2 - c1
r = r2 - r1
if c == 0 and r == 0:
    print(0)
elif c == r or c == -r:
    print(1)
elif abs(c) + abs(r) <= 3:
    print(1)
elif abs(c) + abs(r) <= 6:
    print(2)
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    print(2)
elif (abs(c) + abs(r)) % 2 == 0:
    print(2)
else:
    print(3)
