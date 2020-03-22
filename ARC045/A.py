a = list(input().split())
ans = []
for i in range(len(a)):
    if a[i] == 'Left':
        ans.append('<')
    elif a[i] == 'Right':
        ans.append('>')
    elif a[i] == 'AtCoder':
        ans.append('A')
print(*ans)
