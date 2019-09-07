n = int(input())

if n == 0:
    print(0)
else:
    s = ''
    while n != 0:
        if n % 2 != 0:
            n -= 1
            s = '1' + s
        else:
            s = '0' + s
        n //= -2
    print(s)
