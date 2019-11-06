n = int(input())
a = list(map(int, input().split()))

b = []
if n % 2 == 0:
    for i in range(n//2):
        b.append(a[-1-i*2])
    for i in range(n//2):
        b.append(a[i*2])
else:
    for i in range(n//2+1):
        b.append(a[-1-i*2])
    for i in range(0, n//2):
        b.append(a[1+i*2])
print(' '.join(map(str, b)))
