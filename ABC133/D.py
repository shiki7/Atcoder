n = int(input())
a = list(map(int, input().split()))

# x[0] = sum(a) - 2*(a[1]+a[3]+...)
b = 0
for i in range(1, n-1, 2):
    b += a[i]
x = [sum(a) - 2*b]

for i in range(0, n-1):
    x.append(2*a[i]-x[i])
print(' '.join(map(str, x)))
