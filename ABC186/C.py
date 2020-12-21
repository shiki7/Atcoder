N = int(input())
ans = 0
for i in range(1, N+1):
    if not ('7' in str(i) or '7' in str(oct(i))):
        ans += 1
print(ans)
