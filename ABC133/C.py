L, R = map(int, input().split())
ans = float('inf')
for i in range(L, R+1):
    for j in range(i+1, R+1):
        ans = min(ans, i * j % 2019)
        if ans == 0:
            print(0)
            exit()
print(ans)
