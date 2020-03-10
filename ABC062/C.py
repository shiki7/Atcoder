H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
else:
    ans = float('inf')

    # 横と縦の切るところを真ん中に固定してそれぞれのパターンを線形検索
    center = W//2
    for i in range(1, H):
        # 縦を先に割る
        a1 = center * H
        a2 = (W-center) * i
        a3 = (W-center) * (H-i)

        # 横を先に割る
        b1 = i * W
        b2 = (H-i) * center
        b3 = (H-i) * (W-center)
        ans = min(ans, max(a1, a2, a3) - min(a1, a2, a3))
        ans = min(ans, max(b1, b2, b3) - min(b1, b2, b3))

    center = H//2
    for i in range(1, W):
        # 縦を先に割る
        a1 = i * H
        a2 = (W-i) * center
        a3 = (W-i) * (H-center)

        # 横を先に割る
        b1 = center * W
        b2 = (H-center) * i
        b3 = (H-center) * (W-i)
        ans = min(ans, max(a1, a2, a3) - min(a1, a2, a3))
        ans = min(ans, max(b1, b2, b3) - min(b1, b2, b3))

    # 3つに分割
    ans = min(ans, (H//3+1)*W - (H//3)*W)
    ans = min(ans, (W//3+1)*H - (W//3)*H)

    print(ans)
