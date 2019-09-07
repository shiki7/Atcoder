S = input()
if S[0] == 'A' and 'C' in S[2:-1] and S.count('C') == 1:
    S = S.replace('A', '')
    S = S.replace('C', '')
    if S.islower():
        print('AC')
        exit()
print('WA')
