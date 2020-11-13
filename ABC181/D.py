from collections import Counter

a = list(input())

if len(a) == 1:
    if int(a[0]) % 8 == 0:
        print('Yes')
        exit()
elif len(a) == 2:
    if int(a[0]+a[1]) % 8 == 0 or int(a[1]+a[0]) % 8 == 0:
        print('Yes')
        exit()
else:
    cnt = Counter(a)
    for i in range(112, 1000, 8):
        cnt2 = Counter(list(str(i)))
        flg = True
        for k, v in cnt2.items():
            if cnt[k] < v:
                flg = False
        if flg:
            print('Yes')
            exit()
print('No')
