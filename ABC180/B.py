n = int(input())
x = list(map(int, input().split()))
a = 0
b = 0
c = 0
for i in range(n):
    a += abs(x[i])
    b += x[i]**2
    c = max(abs(x[i]), c)
print(a)
print(b**0.5)
print(c)
