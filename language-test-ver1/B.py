a = input()
b = input()
ans = ''
for i in range(len(b)):
    if b[i] != a:
        ans += b[i]
print(ans)
