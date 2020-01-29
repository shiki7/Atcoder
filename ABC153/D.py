H = int(input())
a = 0
for i in range(0, 10**7):
    if H == 1:
        a = i
        break
    H = H // 2
ans = 0
for i in range(0, a+1):
    ans += 2**i
print(ans)
