n = input()

for i in range(1, 4):
    if n[0] != n[i]:
        print('DIFFERENT')
        exit()
print('SAME')
