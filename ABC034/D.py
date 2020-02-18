# 平均最大化 ＋二分探索
def check(mid, wp, k):
    arr = []
    for i in range(n):
        w = wp[i][0]
        p = wp[i][1]
        arr.append(w * (p-mid))
    return sum(sorted(arr, reverse=True)[:k]) > 0


n, k = map(int, input().split())
wp = [list(map(int, input().split())) for _ in range(n)]
left = 0
right = 100

# 試行回数は100回ぐらいでも通るかも..
for i in range(1000):
    mid = (left+right)/2
    if check(mid, wp, k):
        left = mid
        ans = mid
    else:
        right = mid
        ans = mid
print(ans)
