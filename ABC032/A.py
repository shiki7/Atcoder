a = int(input())
b = int(input())
n = int(input())

for x in range(n, 10**8):
    if x % a == 0 and x % b == 0:
        print(x)
        exit()
