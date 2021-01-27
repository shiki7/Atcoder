N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
total = 0
for i in range(N):
    total += min(L[2*i], L[2*i+1])
print(total)
