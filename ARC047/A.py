N, L = map(int, input().split())
S = input()
count = 1
ans = 0
for i in range(N):
    if S[i] == '+':
        count += 1
    else:
        count -= 1
    if count > L:
        ans += 1
        count = 1
print(ans)
