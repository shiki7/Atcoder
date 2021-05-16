N = int(input())
S, T = [], []
for _ in range(N):
    a = input().split()
    S.append(a[0])
    T.append(int(a[1]))
x = sorted(T)
for i in range(N):
    if x[-2] == T[i]:
        print(S[i])
        exit()
