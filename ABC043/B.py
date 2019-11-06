s = input()
ans = ''
for i in range(len(s)):
    if s[i] == '0' or s[i] == '1':
        ans += s[i]
    elif s[i] == 'B':
        ans = ans[:-1]
print(ans)
