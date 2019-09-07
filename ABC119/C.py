import math

N, A, B, C = map(int, input().split())
l_list = [int(input()) for _ in range(N)]

# それぞれのl_listの竹を Aで使う or Bで使う or Cで使う or 使わないのどれかを全探索してA,B,Cを構築する
# 消費MPは 長さを増やす、減らす:1, 合成する:10


# 深さ優先探索で全探索する cur:現在の竹, used_count:合成された竹の数
def dfs(cur, a, b, c, used_count):
    # Nまで決まったら合成する
    if cur == N:
        # A,B,Cに使われた竹がないということは解答なしでINFを返す
        if a == 0 or b == 0 or c == 0:
            return math.inf
        # 誤差分はMP1で調整 ＋ 合成分はMP10 * (使用した本数 -3)  ※3を引いているのは元のぶんは合成にカウントしないから
        else:
            return abs(a - A) + abs(b - B) + abs(c - C) + (used_count - 3) * 10
    res = math.inf
    res = min(res, dfs(cur + 1, a + l_list[cur], b, c, used_count + 1))
    res = min(res, dfs(cur + 1, a, b + l_list[cur], c, used_count + 1))
    res = min(res, dfs(cur + 1, a, b, c + l_list[cur], used_count + 1))
    res = min(res, dfs(cur + 1, a, b, c, used_count))
    return res


print(dfs(0, 0, 0, 0, 0))
