N = int(input())
a = list(input() for _ in range(N))
b = []
for i in range(N):
    b.append([a[i], int(a[i])])
b = sorted(b, key=lambda x: len(x[0]), reverse=True)
b = sorted(b, key=lambda x: x[1])

for i in range(N):
    print(b[i][0])
