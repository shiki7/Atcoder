N, K = map(int, input().split())
S = list(input())
for i in range(K-1, N):
    if S[i].islower():
        S[i] = S[i].upper()
    else:
        S[i] = S[i].lower()
print(''.join(S))
