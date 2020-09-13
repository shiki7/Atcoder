n = int(input())
if n == 1:
    print(0)
    exit()

mod = 10**9 + 7
print((pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod)
