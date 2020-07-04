S = input() + " "
memo = ""
user = []
flg = False
for i in range(len(S)):
    if S[i] == " ":
        if memo:
            user.append(memo)
        memo = ""
        flg = False
    if S[i] == '@':
        flg = True
        if memo:
            user.append(memo)
        memo = ""
    if flg and S[i] != "@":
        memo += S[i]
for ans in sorted(set(user)):
    print(ans)
