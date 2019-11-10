n = int(input())

total = 0
for i in range(1, n+1):
    total += 10000 * i
print(total//n)
