n = input()
a = ''
count = 0
for i in n:
    if a == i:
        count += 1
    else:
        count = 1
        a = i
    if count == 3:
        print('Yes')
        exit()
print('No')
