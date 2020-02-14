s = input()
ans = ''
for i in range(len(s)):
    if s[i].isdigit():
        ans += s[i]
print(ans)
