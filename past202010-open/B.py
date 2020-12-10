X, Y = map(int, input().split())
if Y == 0:
    print('ERROR')
else:
    print('{:.2f}'.format((X*100 // Y) / 100))
