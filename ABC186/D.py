from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)
b = list(accumulate(sorted_A))
ans = 0
for i in range(N):
    ans += abs((b[-1] - b[i]) - (N-i-1)*sorted_A[i])
print(ans)
