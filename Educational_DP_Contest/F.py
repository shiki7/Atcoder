s = input()
t = input()

len_s = len(s)
len_t = len(t)

# LCSの最長を求める
dp = [[0] * (len_t+1) for _ in range(len_s + 1)]
for i in range(len_s):
    for j in range(len_t):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

# DPを後ろから遡っていって、LCSを求める
lcs_str = ''
i, j = len_s-1, len_t-1
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        lcs_str += s[i]
        i -= 1
        j -= 1
    else:
        if dp[i][j+1] > dp[i+1][j]:
            i -= 1
        else:
            j -= 1
print(lcs_str[::-1])
