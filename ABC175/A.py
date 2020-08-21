a = input()
ans = 0
max_ans = 0
for i in range(3):
    if a[i] == 'R':
        ans += 1
    else:
        max_ans = max(ans, max_ans)
        ans = 0
print(max(ans, max_ans))
