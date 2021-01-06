N = int(input())
AB = list(list(map(int, input().split())) for _ in range(N))

total_a = 0
total_b = 0
c = []
for i in range(N):
    c.append([AB[i][0], AB[i][1], AB[i][0]*2 + AB[i][1]])
    total_a += AB[i][0]
c = sorted(c, key=lambda x: x[2], reverse=True)

for i in range(N):
    total_a -= c[i][0]
    total_b += c[i][0] + c[i][1]
    if total_a < total_b:
        print(i+1)
        exit()
