n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        if not(a[i] % 3 == 0 or a[i] % 5 == 0):
            print('DENIED')
            exit()
print('APPROVED')
