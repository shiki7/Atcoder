S = input()
a, b = 0, 0
c = len(S) % 2
for i in range(len(S)):
    if i % 2 == c:
        a += int(S[i])
    else:
        b += int(S[i])
print(a, b)
