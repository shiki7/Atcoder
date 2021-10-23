S = input()
T = input()
cnt = 0
a = []
for i in range(len(S)):
    if S[i] != T[i]:
        cnt += 1
        a.append(i)
if cnt == 0:
    print('Yes')
elif cnt == 2 and a[0] + 1 == a[1] and S[a[0]] == T[a[1]] and S[a[1]] == T[a[0]]:
    print('Yes')
else:
    print('No')
