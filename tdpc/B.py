A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1 for i in range(B+1)] for j in range(A+1)]
dp[A][B] = 0

for i in range(A, -1, -1):
    for j in range(B, -1, -1):
        if i == A and j == B:
            continue
        elif (i+j) % 2 != 0:
            if j == B:
                dp[i][j] = dp[i+1][j]
            elif i == A:
                dp[i][j] = dp[i][j+1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])
        else:
            if j == B:
                dp[i][j] = dp[i+1][j] + a[i]
            elif i == A:
                dp[i][j] = dp[i][j+1] + b[j]
            else:
                dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j+1] + b[j])

print(dp[0][0])
