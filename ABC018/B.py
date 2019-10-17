s = input()
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    left = lr[i][0] - 1
    right = lr[i][1] - 1
    temp = s[left:right + 1]
    s = s[:left] + temp[::-1] + s[right + 1:]
print(s)
