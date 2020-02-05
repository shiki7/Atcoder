s = input()
t = s.replace('BC', 'D')
a_count = 0
ans = 0
for i in range(len(t)):
    if t[i] == 'A':
        a_count += 1
    elif t[i] == 'D':
        ans += a_count
    else:
        a_count = 0
print(ans)
