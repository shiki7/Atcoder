n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
total = 0
for i in range(n):
    total += m[i]
print(((x - total) // min(m)) + n)
