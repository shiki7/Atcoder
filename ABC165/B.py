x = int(input())
a = 100
for i in range(1, 10**6):
    a += int(a * 0.01)
    if a >= x:
        print(i)
        exit()
