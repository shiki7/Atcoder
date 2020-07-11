S = input()
for i in range(len(S) // 2):
    if not (S[i] == S[-1-i] or S[i] == "*" or S[-1-i] == "*"):
        print('NO')
        exit()
print('YES')
