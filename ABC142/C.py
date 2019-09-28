n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([i, a[i]])
b = sorted(b, key=lambda x: x[1])
c = []
for k, v in b:
    c.append(k+1)
print(' '.join(map(str, c)))
