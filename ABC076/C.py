s = input()
t = input()


flag = False
for i in reversed(range(len(s)-len(t)+1)):
    count = 0
    for j in range(len(t)):
        if s[i+j] == t[j] or s[i+j] == '?':
            count += 1
        else:
            break
    if count == len(t):
        flag = True
        list_s = list(s)
        list_t = list(t)
        list_s[i:i+len(t)] = list_t
        s = ''.join(list_s).replace('?', 'a')
        break
if flag:
    print(s)
else:
    print('UNRESTORABLE')
