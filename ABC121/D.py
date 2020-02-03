a, b = map(int, input().split())

# f(a,b) = f(0,a-1) ^ f(0,b)

# 0からxまでのxorの計算
def calc_xor(x):
    if (x+1) % 2 == 0:
        if (x+1) // 2 % 2 == 0:
            return 0
        else:
            return 1
    else:
        if x // 2 % 2 == 0:
            return 0 ^ x
        else:
            return 1 ^ x

print(calc_xor(a-1) ^ calc_xor(b))
