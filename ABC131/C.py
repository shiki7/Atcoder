def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a, b):
    x = a * b // gcd(a, b)
    return x


a, b, c, d = map(int, input().split())
lcm_cd = lcm(c, d)
a -= 1

x = b - ((b // c + b // d) - (b // lcm_cd))
y = a - ((a // c + a // d) - (a // lcm_cd))
print(x - y)
