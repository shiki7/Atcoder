S = input()
if S[0] == S[1] == S[2] == S[3]:
    print('Weak')
    exit()
for i in range(1, 4):
    if S[i] == '0':
        if S[i-1] != '9':
            print('Strong')
            exit()
    else:
        if int(S[i]) - int(S[i-1]) != 1:
            print('Strong')
            exit()
print('Weak')
