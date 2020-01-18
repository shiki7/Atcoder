s = list(input())
before = s[0]
ans = 1
tmp = ""

for i in range(1, len(s)):
    tmp += s[i]
    if tmp != before:
        ans += 1
        before = tmp
        tmp = ""
print(ans)
