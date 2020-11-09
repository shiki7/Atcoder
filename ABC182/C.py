s = input()
total = 0
cnt1 = 0
cnt2 = 0
for i in range(len(s)):
    total += int(s[i])
    if int(s[i]) % 3 == 1:
        cnt1 += 1
    elif int(s[i]) % 3 == 2:
        cnt2 += 1
if total % 3 == 0:
    print(0)
    exit()
if total % 3 == 1:
    if cnt1 >= 1 and len(s) > 1:
        print(1)
    elif cnt2 >= 2 and len(s) > 2:
        print(2)
    else:
        print(-1)
else:
    if cnt2 >= 1 and len(s) > 1:
        print(1)
    elif cnt1 >= 2 and len(s) > 2:
        print(2)
    else:
        print(-1)
