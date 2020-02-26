n, m, a, b = map(int, input().split())
c = [int(input()) for _ in range(m)]

for i in range(m):
    if n <= a:
        n += b
    if n >= c[i]:
        n -= c[i]
    else:
        print(i+1)
        exit()
print('complete')
