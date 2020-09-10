n = int(input())
s = list(list(input())[::-1] for _ in range(n))[::-1]
for i in range(1, n):
    for j in range(i, i+2*(n-i-1)+1):
        if s[i-1][j-1] == "X" or s[i-1][j] == 'X' or s[i-1][j+1] == 'X':
            s[i][j] = "X"
for i in range(n):
    print(''.join(s[-i-1][::-1]))
