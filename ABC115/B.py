n = int(input())
p = [int(input()) for _ in range(n)]
max_p = max(p)
print(sum(p)-max_p//2)
