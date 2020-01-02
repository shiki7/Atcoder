import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


n = int(input())
for i in range(n, 10**10):
    if is_prime(i):
        print(i)
        exit()
