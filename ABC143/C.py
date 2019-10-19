n = int(input())
s = input()


for i in range(n):
    if i == 0:
        ans = s[i]
    elif ans[-1] != s[i]:
        ans += s[i]
print(len(ans))
