N, M = map(int, input().split())
shop = []
for i in range(N):
    shop.append(list(map(int, input().split())))

shop.sort()

total = 0
for i in range(len(shop)):
    if shop[i][1] == M:
        total += shop[i][0] * shop[i][1]
        break
    elif shop[i][1] > M:
        total += shop[i][0] * M
        break
    else:
        total += shop[i][0] * shop[i][1]
        M -= shop[i][1]
print(total)
