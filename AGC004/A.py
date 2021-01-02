a = list(map(int, input().split()))
for i in range(3):
    if a[i] % 2 == 0:
        print(0)
        exit()
a = sorted(a)
print(a[0]*a[1])
