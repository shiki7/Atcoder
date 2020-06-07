E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))
count = len(set(E) & set(L))
if count == 6:
    print(1)
elif count == 5:
    if B in L:
        print(2)
    else:
        print(3)
elif count == 4:
    print(4)
elif count == 3:
    print(5)
else:
    print(0)
