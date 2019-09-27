n = int(input())
max_count = 0
ans = 1
for i in range(1, n + 1):
    x = i
    for j in range(1, n):
        if x % 2 == 0:
            x //= 2
        else:
            if j > max_count:
                max_count = j
                ans = i
            break
print(ans)
