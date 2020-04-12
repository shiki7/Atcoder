S, L, R = map(int, input().split())
if L <= S <= R:
    print(S)
elif S > R:
    print(R)
else:
    print(L)
