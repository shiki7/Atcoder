a, b = map(int, input().split())
ans = 0
for x in range(a, b + 1):
    str_x = str(x)
    if str_x == str_x[::-1]:
        ans += 1
print(ans)
