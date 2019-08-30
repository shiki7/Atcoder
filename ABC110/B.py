N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

MAX_X = max(x)
MIN_Y = min(y)
for num in range(X + 1, Y + 1):
    if num > MAX_X and num <= MIN_Y:
        print('No War')
        exit()
print('War')
