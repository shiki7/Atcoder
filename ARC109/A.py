a, b, x, y = map(int, input().split())
if a == b:
    print(x)
    exit()
if 2*x < y:
    if b - a < 0:
        print(x*abs(b-a)*2-x)
    else:
        print(x*abs(b-a)*2+x)
else:
    if b-a < 0:
        print(x+(abs(b-a)-1)*y)
    else:
        print(x+(abs(b-a))*y)
