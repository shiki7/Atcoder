s = input()
s_sorted = sorted(list(set(s)))
for i in range(97, 97+26):
    if chr(i) not in s_sorted:
        print(chr(i))
        exit()
    else:
        s_sorted.remove(chr(i))
print('None')
