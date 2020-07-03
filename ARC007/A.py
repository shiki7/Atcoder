X = input()
S = input()
ans = ''
for i in range(len(S)):
    if S[i] != X:
        ans += S[i]
print(ans)
