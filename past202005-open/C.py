A, R, N = map(int, input().split())
a = A
if R == 1:
    if A <= 10**9:
        print(A)
        exit()
    else:
        print('large')
for _ in range(N-1):
    a *= R
    if a > 10**9:
        print('large')
        exit()
print(a)
