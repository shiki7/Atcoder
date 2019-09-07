N = int(input())
b = list(map(int, input().split()))

total = b[-1]
for i in range(1, len(b)):
    total += min(b[-i], b[-i-1])
total += b[0]
print(total)
