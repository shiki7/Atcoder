N = int(input())
ans = []
for i in range(N):
    c = int(input())
    s = set(input().split())
    if i == 0:
        ans = s
    else:
        ans = ans & s
print(len(ans))
