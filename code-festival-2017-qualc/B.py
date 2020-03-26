N = int(input())
A = list(map(int, input().split()))

even_cnt = 0
for i in range(N):
    if A[i] % 2 == 0:
        even_cnt += 1
print(3**N - 2**even_cnt)
