n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
count = 0


def dfs(i, switch):
    if i == n:
        # check
        light_on_flag = True
        for a in range(m):
            switch_on_count = 0
            for b in range(ks[a][0]):
                if switch[ks[a][b + 1] - 1]:
                    switch_on_count += 1
            if not switch_on_count % 2 == p[a]:
                light_on_flag = False
                break
        if light_on_flag:
            global count
            count += 1
        return

    switch[i] = True
    dfs(i + 1, switch)
    switch[i] = False
    dfs(i + 1, switch)


switch = [False] * n
dfs(0, switch)
print(count)
