s = input()

dic = {}
for char in 'abc':
    dic[char] = s.count(char)

min_val = min(dic.values())
for k in dic:
    if dic[k] - min_val > 1:
        print('NO')
        exit()
print('YES')
