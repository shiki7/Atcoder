n = int(input())
if n < 2:
    print(0)
    exit()

if n % 2 != 0:
    print(0)
    exit()

ans = 0
a = 10
for i in range(10**18):
    if 10*5**i > n:
        break
    ans += n//(10*5**i)
print(ans)
