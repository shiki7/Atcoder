# TLEになる
# TODO: DPで解きなおす
S = input()
N = len(S)
ans = 0
for i in range(N-3):
    for j in range(i+3, N):
        if int(S[i:j+1]) % 2019 == 0:
            ans += 1
print(ans)
