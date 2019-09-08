N = int(input())


def is_divisor_counter8(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return True if count == 8 else False


count = 0
for i in range(1, N+1, 2):
    if is_divisor_counter8(i):
        count += 1
print(count)
