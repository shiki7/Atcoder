a = input()
b = input()
ans = ''
for i in range(max(len(a), len(b))):
    if i < len(a):
        ans += a[i]
    if i < len(b):
        ans += b[i]
print(ans)
