N = int(input())
for _ in range(N):
    a = int(input())
    if a % 4 == 0:
        print('Even')
    elif a % 2 == 0:
        print('Same')
    else:
        print('Odd')
