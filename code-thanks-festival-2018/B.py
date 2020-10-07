a, b = map(int, input().split())

if (a + b) % 4 != 0:
    print('No')
    exit()
if a > 3*b or 3*a < b:
    print('No')
    exit()

cnt = (a+b) // 4
if (a - cnt) % 2 == 0 and (b-cnt) % 2 == 0:
    print('Yes')
else:
    print('No')
