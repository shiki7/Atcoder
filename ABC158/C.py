A, B = map(int, input().split())

n = 10**6
for i in range(n):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        exit()
    elif int(i * 0.08) > A or int(i * 0.01) > B:
        print(-1)
        exit()
