n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(i+1)

b = 0
for _ in range(m):
    i = int(input())
    for j in range(n):
        if a[j] == i:
            tmp = a[j]
            a[j] = b
            b = tmp
            break

for i in range(n):
    print(a[i])
