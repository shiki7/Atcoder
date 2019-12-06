x = input()

n = len(x)
mylist = ['c', 'h', 'o', 'k', 'u']
for i in range(n):
    if x[i] not in mylist:
        print('NO')
        exit()
    if x[i] == 'c':
        if i == n-1:
            print('NO')
            exit()
        else:
            if x[i+1] != 'h':
                print('NO')
                exit()
    if x[i] == 'h':
        if i == 0:
            print('NO')
            exit()
        if x[i-1] != 'c':
            print('NO')
            exit()
print('YES')
