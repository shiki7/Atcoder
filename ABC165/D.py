A, B, N = map(int, input().split())

# f(x+B) = f(x)
# 単調増加
x = min(B-1, N)
ans = (A*x)//B - A*(x//B)
print(ans)
