n = int(input())
a = list(map(int, input().split()))

b = [0] * 200001
x = 0
for i in range(n):
    b[a[i]] = 1
    for j in range(x, n+1):
        if b[j] == 0:
            print(j)
            break
        else:
            x = j+1
