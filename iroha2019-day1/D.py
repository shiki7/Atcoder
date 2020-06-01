N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(N):
    if i % 2 == 0:
        X += A[i]
    else:
        Y += A[i]

if X == Y:
    print('Draw')
elif X > Y:
    print('Takahashi')
else:
    print('Aoki')
