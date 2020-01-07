s = input() + '#'

odd_count = 0
even_count = 0
t = [0] * len(s)
flag = True
for i in range(len(s)):
    if flag:
        if s[i] == 'R':
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            flag = False
            pos = i
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    else:
        if s[i] == 'R' or s[i] == '#':
            if pos % 2 == 0:
                t[pos-1] = odd_count
                t[pos] = even_count
            else:
                t[pos-1] = even_count
                t[pos] = odd_count
            if i % 2 == 0:
                even_count = 1
                odd_count = 0
            else:
                even_count = 0
                odd_count = 1
            flag = True
        else:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
print(' '.join(map(str, t[:-1])))
