M, D = map(int, input().split())
count = 0
for i in range(22, D+1):
    str_i = str(i)
    if int(str_i[0]) < 2 or int(str_i[1]) < 2:
        continue
    if int(str_i[0]) * int(str_i[1]) <= M:
        count += 1
print(count)
