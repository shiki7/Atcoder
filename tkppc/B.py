N = int(input())
a = list(int(input()) for _ in range(N))
max_a = 0
ans = 1
for i in range(N):
    if a[i] > max_a:
        ans = i + 1
        max_a = a[i]
print(ans)
