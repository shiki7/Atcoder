S = input()
for i in range(len(S)):
    if i % 2 == 1:
        if not S[i] in ['L', 'U', 'D']:
            print('No')
            exit()
    else:
        if not S[i] in ['R', 'U', 'D']:
            print('No')
            exit()
print('Yes')
