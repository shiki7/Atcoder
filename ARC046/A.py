n = int(input())
a = n // 9
b = n % 9

if b == 0:
    print('9'*a)
else:
    print(str(b) * (a+1))
