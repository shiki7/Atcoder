a, b = map(int, input().split())
if a == 1 and b == 1:
    print('Draw')
elif a == 1:
    print('Alice')
elif b == 1:
    print('Bob')
elif a == b:
    print('Draw')
elif a < b:
    print('Bob')
elif a > b:
    print('Alice')
