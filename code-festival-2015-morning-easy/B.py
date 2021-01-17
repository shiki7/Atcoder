N = int(input())
S = input()
cnt = 0
if N % 2 == 1:
    print(-1)
    exit()
for i in range(N//2):
    if S[i] != S[i+N//2]:
        cnt += 1
print(cnt)
