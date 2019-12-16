n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

flag = True
pairs = []
for i in range(1, len(a)):
    if flag:
        if a[i] == a[i-1]:
            pairs.append(a[i])
            if len(pairs) == 2:
                print(pairs[0]*pairs[1])
                exit()
            flag = False
    else:
        flag = True
print(0)
