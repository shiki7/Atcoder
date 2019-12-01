import math
n = int(input())
min_n = int(n // 1.08)
max_n = math.ceil(n / 1.08)

for x in range(min_n, max_n+1):
    if math.floor(x * 1.08) == n:
        print(x)
        exit()
print(":(")
