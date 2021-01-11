N = int(input())
S = input()
t = ""
for i in range(N):
    tmp = ""
    for j in range(len(t)):
        if t[j] != S[i]:
            tmp += t[j]
    t = tmp + S[i]
print(t)
