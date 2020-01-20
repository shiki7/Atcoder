N = int(input())
 
# 1, 6, 9 の階乗の組み合わせの合計が N
ans = N
for i in range(N + 1):
    cnt = 0
    total = i
    while total > 0:
        cnt += total % 6
        total //= 6
    j = N - i
    while j > 0:
        cnt += j % 9
        j //= 9
    ans = min(ans, cnt)
print(ans)
