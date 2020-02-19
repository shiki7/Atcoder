x = input()
count_s = 0
ans = 0
for i in range(len(x)):
    if x[i] == 'S':
        count_s += 1
    if x[i] == 'T':
        if count_s == 0:
            ans += 1
        else:
            count_s -= 1
ans += count_s
print(ans)
