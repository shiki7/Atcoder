n = int(input())
s = input()
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ''
for i in range(len(s)):
    ans += char[(ord(s[i])-65+n) % 26]
print(ans)
