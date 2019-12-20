n = int(input())

def dfs(count, s):
    if int(s) > n:
        return count
    if '3' in s and '5' in s and '7' in s:
        count += 1
    for c in '357':
        count = dfs(count, s+c)
    return count

print(dfs(0, '0'))
