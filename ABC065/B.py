n = int(input())
a = [int(input()) for _ in range(n)]
button = [1] + [0] * (n - 1)
i = 0
count = 0
for _ in range(n):
    count += 1
    if button[i] == 1:
        button[i] = 0
        button[a[i] - 1] = 1
        i = a[i] - 1
    else:
        print(-1)
    if button[1] == 1:
        print(count)
        exit()
print(-1)
