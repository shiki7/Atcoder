s = input()
a = s.split('+')
ans = 0
for x in a:
    if "0" not in x:
        ans += 1
print(ans)
