S = input()
A = set(S)

ans = float('inf')
for a in A:
    cnt = 0
    cnt_list = []
    for i in range(len(S)):
        if S[i] == a:
            cnt_list.append(cnt)
            cnt = 0
        else:
            cnt += 1
    cnt_list.append(cnt)
    ans = min(ans, max(cnt_list))
print(ans)
