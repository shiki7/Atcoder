import fractions

N = int(input())
a = list(map(int, input().split()))

# 最小公倍数
lcm = a[0]
for i in range(1, N):
    lcm = lcm * a[i] // fractions.gcd(lcm, a[i])

total = 0
for i in range(N):
    total += (lcm - 1) % a[i]
print(total)
