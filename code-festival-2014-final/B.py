S = input()
ans = 0
for i in range(len(S)):
    if i % 2 == 0:
        ans += int(S[i])
    else:
        ans -= int(S[i])
print(ans)
