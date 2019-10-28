n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h = sorted(h)
min_ans = 10**10
for i in range(n - k + 1):
    min_ans = min(min_ans, h[i + k - 1] - h[i])
print(min_ans)
