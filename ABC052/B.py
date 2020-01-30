n = int(input())
s = input()
 
count = 0
ans = 0
for x in s:
    if x == 'I':
        count += 1
    elif x == 'D':
        count -= 1
    ans = max(count, ans)
print(ans)
