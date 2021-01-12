N = int(input())
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""
if N // (36**2) >= 1:
    ans += S[N // (36**2)]
    N -= (N//(36**2)) * (36**2)
if N // 36 >= 1:
    ans += S[N // 36]
    N -= (N//36) * 36
ans += S[N]
print(ans)
