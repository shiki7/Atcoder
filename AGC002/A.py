a, b = map(int, input().split())
if a < 0 and b < 0:
    if (b-a+1) % 2 == 0:
        print('Positive')
    else:
        print('Negative')
elif (a < 0 and b >= 0) or a == 0:
    print('Zero')
else:
    print('Positive')
