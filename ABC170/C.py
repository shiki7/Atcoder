X, N = map(int, input().split())
a = list(map(int, input().split()))
ans = 1
min_diff = float('inf')
for i in range(0, 102):
    if i in a:
        continue
    if (abs(i - X) < min_diff) or (abs(i - X) == min_diff and i < ans):
        min_diff = abs(i - X)
        ans = i
print(ans)
