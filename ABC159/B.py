S = input()
n = len(S)
x = S[0:(n-1)//2]
y = S[(n+3)//2-1:n]
if x == x[::-1] and y == y[::-1] and S == S[::-1]:
    print('Yes')
else:
    print('No')
