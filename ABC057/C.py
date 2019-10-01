import math
n = int(input())
max_num = 0
for i in range(1, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
        max_num = i
print(len(str(n // max_num))
