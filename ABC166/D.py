x = int(input())

a = [i**5 for i in range(1000)]
for i in range(1000):
    for j in range(1000):
        if a[i] - a[j] == x:
            print(i, j)
            exit()
        if a[i] + a[j] == x:
            print(i, -j)
            exit()
