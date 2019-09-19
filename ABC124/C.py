S = input()
n = len(S)
a = b = ''
for i in range(n):
    if i % 2 == 0:
        a += '0'
        b += '1'
    else:
        a += '1'
        b += '0'

diff_a = diff_b = 0
for i in range(n):
    if S[i] != a[i]:
        diff_a += 1
    if S[i] != b[i]:
        diff_b += 1

print(min(diff_a, diff_b))
