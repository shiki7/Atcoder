s = input()
count = 1
ans = ''
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        count += 1
    else:
        ans += s[i-1]+str(count)
        count = 1
    if i == len(s)-1:
        ans += s[i]+str(count)
print(ans)
