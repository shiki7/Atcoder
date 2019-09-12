N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
min_diff = float("inf")
min_idx = 0
for i in range(N):
    diff = abs(A - (T - H[i] * 0.006))
    if min_diff > diff:
        min_diff = diff
        min_idx = i
print(min_idx + 1)
