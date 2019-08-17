# -*- coding: utf-8 -*-
K, X = map(int, input().split())
ans = ""
for i in range(X-K+1, X+K):
    if ans == "":
        ans = str(i)
    else:
        ans = ans + " " + str(i)
print(ans)
