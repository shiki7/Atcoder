import math


def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


n = int(input())
sum_n = (1+n)*n/2
if is_prime(sum_n):
    print('WANWAN')
else:
    print('BOWWOW')
