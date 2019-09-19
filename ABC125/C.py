import fractions
n = int(input())
a = [0] + list(map(int, input().split())) + [0]

# 前処理。left, rightでそれぞれ累積gcdを作っておく
left = [0] * (n + 2)
right = [0] * (n + 2)

for i in range(n):
    left[i] = fractions.gcd(left[i - 1], a[i])

for i in range(n, 0, -1):
    right[i] = fractions.gcd(right[i + 1], a[i])

for i in range(1, n):
    right[-i - 1] = fractions.gcd(right[-i], a[-i - 1])

ans = 1
for i in range(1, n + 1):
    ans = max(ans, fractions.gcd(left[i - 1], right[i + 1]))
print(ans)
