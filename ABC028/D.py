N, K = map(int, input().split())

# k未満、k、kより大きいの並び替え
# 2つがkで残りがそれ以外
# すべてk
print(((K-1) * (N-K) * 6 + (N-1) * 3 + 1) / (N**3))
