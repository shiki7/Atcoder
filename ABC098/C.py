n = int(input())
s = input()

count = [float('inf')] * n

# 左端
count[0] = 0
for i in range(1, n):
    if s[i] == 'E':
        count[0] += 1

# 尺取
for i in range(1, n):
    count[i] = count[i-1]
    if s[i-1] == 'W':
        count[i] += 1
    if s[i] == 'E':
        count[i] -= 1

print(min(count))
