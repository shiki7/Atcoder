n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a, reverse=True)
b = sorted(b, reverse=True)
if n < m:
    print('NO')
    exit()
for i in range(m):
    if b[i] > a[i]:
        print('NO')
        exit()
print('YES')
