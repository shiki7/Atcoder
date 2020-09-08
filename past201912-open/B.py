n = int(input())
x = [int(input()) for _ in range(n)]

for i in range(1, n):
    if x[i] < x[i-1]:
        print('down ' + str(x[i-1]-x[i]))
    elif x[i] > x[i-1]:
        print('up ' + str(x[i]-x[i-1]))
    else:
        print('stay')
