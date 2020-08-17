S, T = input().split()
if S[0] == "B":
    s = -int(S[1])
else:
    s = int(S[0]) - 1
if T[0] == "B":
    t = -int(T[1])
else:
    t = int(T[0]) - 1
print(abs(s-t))
