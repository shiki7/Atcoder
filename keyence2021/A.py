N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(N-1):
    a[i+1] = max(a[i], a[i+1])
c = []
c.append(a[0]*b[0])
for i in range(1, N):
    c.append(max(a[i]*b[i], c[i-1]))
for i in range(N):
    print(c[i])
