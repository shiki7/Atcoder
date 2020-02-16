s = input()
s = s[::-1] + '0'

ans = 0
up = 0
for i in range(len(s)):
    int_s = int(s[i])
    if int_s+up <= 4:
        ans += int_s + up
        up = 0
    elif int_s+up == 5:
        if int(s[i+1]) < 5:
            ans += int_s + up
            up = 0
        else:
            ans += 10 - (int_s + up)
            up = 1
    else:
        ans += 10 - (int_s + up)
        up = 1
print(ans)
