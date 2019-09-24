h, w = map(int, input().split())
s = [['.'] * (w + 2)]
s += [list('.' + input() + '.') for _ in range(h)]
s += [['.'] * (w + 2)]
for i in range(h + 1):
    for j in range(w + 1):
        if s[i][j] != '#':
            count = 0
            if s[i][j + 1] == '#':
                count += 1
            if s[i][j - 1] == '#':
                count += 1
            if s[i - 1][j] == '#':
                count += 1
            if s[i + 1][j] == '#':
                count += 1
            if s[i - 1][j - 1] == '#':
                count += 1
            if s[i + 1][j + 1] == '#':
                count += 1
            if s[i - 1][j + 1] == '#':
                count += 1
            if s[i + 1][j - 1] == '#':
                count += 1
            s[i][j] = count

for i in range(1, h + 1):
    ans = []
    for j in range(1, w + 1):
        ans += str(s[i][j])
    print(''.join(ans))
