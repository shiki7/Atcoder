a = int(input())
b = int(input())
if a * b >= 0:
    print(2*max(abs(a), abs(b)))
else:
    print((abs(a)+abs(b))*2)
