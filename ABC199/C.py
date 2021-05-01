N = int(input())
S = list(input())
Q = int(input())
flipped = False
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flipped:
            a += N
            a %= (2 * N)
            b += N
            b %= (2 * N)
        S[a], S[b] = S[b], S[a]
    else:
        flipped = not flipped
if flipped:
    S = S[N:] + S[:N]
print(''.join(S))
