import math


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


n = int(input())
a = str(n)[-1]
if is_prime(n):
    print('Prime')
    exit()
else:
    if len(make_divisors(n)) > 2:
        if int(a) % 2 != 0 and int(a) != 5 and sum(map(int, list(str(n)))) % 3 != 0:
            print('Prime')
            exit()
print('Not Prime')
