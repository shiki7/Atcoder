N = int(input())
while N % 2 == 0:
    N //= 2
sq_N = int(N**0.5)
ans = 0
for i in range(1, sq_N+1):
    if N % i == 0:
        ans += 1
ans = ans*2-(sq_N**2 == N)
print(ans*2)
