S = input()
N = int(input())
for i in range(N):
    S = S[1:] + S[0]
print(S)
