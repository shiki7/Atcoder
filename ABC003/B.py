s = input()
t = input()

target = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    if s[i] == '@' and t[i] != '@':
        if t[i] not in target:
            print('You will lose')
            exit()
        else:
            continue
    if t[i] == '@' and s[i] != '@':
        if s[i] not in target:
            print('You will lose')
            exit()
        else:
            continue
    if s[i] != t[i]:
        print('You will lose')
        exit()
print('You can win')
