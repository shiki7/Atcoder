n = int(input())
b = list(map(int, input().split()))

ans = []
while len(b) > 0:
    flag = False
    for i in range(len(b)-1, -1, -1):
        if b[i] == i+1:
            ans.append(b[i])
            b.pop(i)
            flag = True
            break
    if not flag:
        print(-1)
        exit()

for i in range(len(ans)):
    print(ans[-i-1])
