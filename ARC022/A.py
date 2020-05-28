S = input()
index = 0
for i in range(len(S)):
    if S[i].lower() == 'i' and index == 0:
        index += 1
    elif S[i].lower() == 'c' and index == 1:
        index += 1
    elif S[i].lower() == 't' and index == 2:
        print('YES')
        exit()
print('NO')
