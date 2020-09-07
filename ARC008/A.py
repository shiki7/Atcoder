import math
n = int(input())
print(min(n // 10 * 100 + n % 10 * 15, math.ceil(n / 10)*100))
