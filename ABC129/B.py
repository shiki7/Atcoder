n = int(input())
w = list(map(int, input().split()))
min_abs = float('inf')
for t in range(1, max(w)):
    for i in range(n):
        min_abs = min(min_abs, abs(sum(w[:i]) - sum(w[i:])))
print(min_abs)
