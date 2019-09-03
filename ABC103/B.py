S = input()
T = input()
for i in range(len(S)):
    if S == T[i:] + T[0:i]:
        print('Yes')
        exit()
print('No')
