S = input()
x, y = S.split('.')
if 0 <= int(y) <= 2:
    print(x + '-')
elif 3 <= int(y) <= 6:
    print(x)
else:
    print(x + '+')
