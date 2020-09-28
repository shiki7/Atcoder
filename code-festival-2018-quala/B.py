n, m, a, b = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]
arr = [0] * n
for i in range(m):
    for j in range(lr[i][0]-1, lr[i][1]):
        if arr[j] == 0:
            arr[j] += 1
print(sum(arr)*a + (n-sum(arr))*b)
