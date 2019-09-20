n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
median = y[n // 2]
for i in range(n):
    if x[i] < median:
        print(median)
    else:
        print(y[n // 2 - 1])
