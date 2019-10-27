# not clear
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
b = prime_factorize(n)
if len(b) == 1:
    print(b[0] - 1)
    exit()
x = 1
y = 1
b = sorted(b, reverse=True)
for i in range(0, len(b)):
    if x <= y:
        x *= b[i]
    else:
        y *= b[i]
print(x+y-2)
