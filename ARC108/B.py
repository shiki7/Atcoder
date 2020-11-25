N = int(input())
S = input()
T = S
cnt = 0
for i in range(N):
    T += S[i]
    if T[-3:] == "fox":
        T = T[:-3]
        cnt += 1
print(N-cnt*3)
