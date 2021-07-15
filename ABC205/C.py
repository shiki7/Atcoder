import math
a, b, c = map(int, input().split())

if a == b:
    print("=")
    exit()
if c % 2 == 0:
    if a == -b:
        print('=')
        exit()
    elif math.fabs(a) > math.fabs(b):
        print(">")
        exit()
    else:
        print("<")
        exit()

if a > b:
    print('>')
elif a < b:
    print('<')
