H, W = map(int, input().split())
grid = ['.' * (W + 2)]
for i in range(H):
    grid.append('.' + input() + '.')
grid += ['.' * (W + 2)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if grid[i][j] == "#":
            if not (grid[i][j + 1] == "#" or grid[i + 1][j] == "#"
                    or grid[i][j - 1] == "#" or grid[i - 1][j] == "#"):
                print('No')
                exit()
print('Yes')
