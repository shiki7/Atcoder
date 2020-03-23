N = int(input())
H = int(input())
W = int(input())
if N > H and N > W:
    print((N-H+1)*(N-W+1))
elif N > H and N == W:
    print(N-H+1)
elif N == H and N > W:
    print(N-W+1)
elif N == H and N == W:
    print(1)
