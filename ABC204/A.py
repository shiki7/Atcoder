a, b = map(int, input().split())
if a == b:
    print(a)
else:
    if a != 0 and b != 0:
        print(0)
    elif a != 1 and b != 1:
        print(1)
    else:
        print(2)
