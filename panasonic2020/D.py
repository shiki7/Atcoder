N = int(input())
w = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def dfs(s, i):
    # s:文字列 i:最大のアルファベットのindex
    if len(s) == N:
        print(s)
    else:
        for k in range(i+2):
            if k == i+1:
                dfs(s+w[k], i+1)
            else:
                dfs(s+w[k], i)


x = dfs('a', 0)
