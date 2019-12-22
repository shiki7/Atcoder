n = int(input())
a = list(map(int, input().split()))

index = 1
ans = 0
for i in range(n):
    if a[i] == index:
        index += 1
    else:
        ans += 1
if index == 1:
    print(-1)
else:
    print(ans)
