import math
n, a = map(int, input().split())
print(math.ceil(a/3), min(n//3, a))
