N = int(input())
H = list(map(int, input().split()))
count = 0
max_count = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(max_count)
