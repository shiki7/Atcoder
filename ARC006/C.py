N = int(input())
w = [int(input()) for _ in range(N)]

arr = []
for i in range(N):
    is_stack = False
    for j in range(len(arr)):
        if arr[j] >= w[i]:
            arr[j] = w[i]
            is_stack = True
            break
    if not is_stack:
        arr.append(w[i])
print(len(arr))
