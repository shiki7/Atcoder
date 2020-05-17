y = int(input())
m = int(input())
d = int(input())

if m == 1 or m == 2:
    m += 12
    y -= 1

y2 = 2014
m2 = 5
d2 = 17


def calc(y, m, d):
    return 365*y+y//4-y//100+y//400+(306*(m+1)//10)+d-429


print(abs(calc(y2, m2, d2) - calc(y, m, d)))
