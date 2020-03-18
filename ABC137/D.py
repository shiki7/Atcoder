import heapq

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

pay_list = []
heapq.heapify(pay_list)
ans = 0
AB = sorted(AB, reverse=True)

for i in range(1, M+1):
    # 実行可能なバイトリストを抽出
    for j in range(len(AB)-1, -1, -1):
        a = AB[j][0]
        b = AB[j][1]
        if a <= i:
            # heappopで最大値を取り出したいため、補正値の(-1)を乗じておく
            heapq.heappush(pay_list, b*(-1))
            AB.pop(j)
        else:
            break
    # 最大の報酬の値を取り出して足す
    if len(pay_list) > 0:
        ans += heapq.heappop(pay_list) * (-1)
print(ans)
