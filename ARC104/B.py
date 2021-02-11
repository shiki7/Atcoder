# pypyじゃないとTLE
N, S = input().split()
ans = 0
for i in range(int(N)):
    cnt1 = 0
    cnt2 = 0
    for j in range(i, int(N)):
        if S[j] == "A":
            cnt1 += 1
        elif S[j] == "T":
            cnt1 -= 1
        elif S[j] == "C":
            cnt2 += 1
        elif S[j] == "G":
            cnt2 -= 1
        if cnt1 == 0 and cnt2 == 0:
            ans += 1
print(ans)
