a, k = map(int, input().split())
if k == 0:
    print(2*(10**12) - a)
    exit()
for i in range(1, 10*7):
    a += 1+k*a
    if a >= 2 * (10**12):
        print(i)
        exit()
