s = int(input())
a = [s]
for i in range(2, 10**6 - 2):
    if s % 2 == 0:
        s //= 2
    else:
        s = s * 3 + 1
    if s in a:
        print(i)
        exit()
    a.append(s)
