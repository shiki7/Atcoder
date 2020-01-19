n, x = map(int, input().split())
a = list(map(int, input().split()))
bin_x = bin(x)[2:]
bin_x_rev = bin_x[::-1]
ans = 0
for i in range(len(bin_x_rev)):
    if bin_x_rev[i] == '1':
        ans += a[i]
print(ans)
