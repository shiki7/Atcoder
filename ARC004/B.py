n = int(input())
d = [int(input()) for _ in range(n)]
print(sum(d))
print(max(0, max(d)*2 - sum(d)))
