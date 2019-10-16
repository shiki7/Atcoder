n = int(input())
h = list(map(int, input().split()))
# 後ろから試行しないと、 「1 2 2 1」のようなパターンに対応できない
for i in range(n - 2, 0, -1):
    if h[i] - h[i + 1] >= 1:
        h[i] -= 1
for i in range(n - 1):
    if h[i + 1] < h[i]:
        print('No')
        exit()
print('Yes')
