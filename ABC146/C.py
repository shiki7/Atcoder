a, b, x = map(int, input().split())

ans = 0
max_digit = 0

for i in range(1, 19):
    num = 10 ** (i - 1)
    if a * num + b * len(str(num)) <= x:
        max_digit = max(max_digit, i)
    else:
        break
if max_digit == 0:
    print(0)
    exit()
if max_digit > 10:
    max_digit = 10
ans = (x - b * (max_digit)) // a
if ans >= 10**9:
    print(10**9)
    exit()
print(ans)
