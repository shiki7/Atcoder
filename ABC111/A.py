n = input()
ans = ''
for num in n:
    if num == '1':
        ans += '9'
    elif num == '9':
        ans += '1'
    else:
        ans += num
print(ans)
