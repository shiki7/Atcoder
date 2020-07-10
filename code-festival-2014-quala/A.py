n = int(input())
for i in range(10**5):
    if i**3 == n:
        print('YES')
        exit()
    if i**3 > n:
        print('NO')
        exit()
