s = input()
t = int(input())
x = 0
y = 0
q = 0
for a in s:
    if a == 'L':
        x -= 1
    elif a == 'R':
        x += 1
    elif a == 'U':
        y += 1
    elif a == 'D':
        y -= 1
    elif a == '?':
        q += 1
if t == 1:
    print(abs(x) + abs(y) + q)
else:
    if abs(x) + abs(y)-q < 0:
        if (abs(x) + abs(y)-q) % 2 == 0:
            print(0)
        else:
            print(1)
    else:
        print(abs(x) + abs(y)-q)
