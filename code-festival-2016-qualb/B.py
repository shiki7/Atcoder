n, a, b = map(int, input().split())
s = input()

count = 0
countB = 0
for i in range(n):
    if s[i] == 'a':
        if count < a+b:
            print('Yes')
            count += 1
        else:
            print('No')
    elif s[i] == 'b':
        if count < a+b and countB < b:
            print('Yes')
            count += 1
            countB += 1
        else:
            print('No')
    else:
        print('No')
