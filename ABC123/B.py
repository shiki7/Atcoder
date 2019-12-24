a = [int(input()) for _ in range(5)]
b = []
ans = 0
for i in range(5):
    if a[i] % 10 == 0:
        ans += a[i]
    else:
        b.append([a[i], a[i] % 10])
sorted_b = sorted(b, key=lambda x: x[1], reverse=True)

for i in range(len(sorted_b)):
    if i == len(sorted_b) - 1:
        ans += sorted_b[i][0]
    else:
        ans += sorted_b[i][0] + (10 - sorted_b[i][1])
print(ans)
