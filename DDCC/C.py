h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]

idx = 1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            s[i][j] = idx
            idx += 1
# 横一列を埋める
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if j != 0:
                s[i][j] = s[i][j-1]
            else:
                for k in range(1, w-j):
                    if s[i][j+k] != ".":
                        s[i][j] = s[i][j+k]
                        break
# 横一列埋まっていない場合、縦に見る
for i in range(h):
    if s[i][0] == ".":
        if i != h-1:
            for j in range(1, h-i):
                if s[i+j][0] != ".":
                    for k in range(0, w):
                        s[i][k] = s[i+j][k]
                    break
        else:
            for j in range(1, h):
                if s[i-j][0] != ".":
                    for k in range(0, w):
                        s[i][k] = s[i-j][k]
                    break
for i in range(h):
    tmp_list = map(str, s[i])
    print(' '.join(tmp_list))
