import math

n = int(input())
a = math.ceil(math.sqrt(n))
min_ans = float('inf')

for i in range(1, a+1):
    if n % i == 0:
        min_ans = min(min_ans, i+n//i-2)
print(min_ans)
