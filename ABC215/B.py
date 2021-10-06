N = int(input())
a = 1
for i in range(1, 10**5):
    a *= 2
    if a > N:
        print(i - 1)
        exit()
