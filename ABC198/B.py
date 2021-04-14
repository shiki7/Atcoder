S = input()
for i in range(10):
    tmp = "0" * i + S
    if tmp == tmp[::-1]:
        print('Yes')
        exit()
print('No')
