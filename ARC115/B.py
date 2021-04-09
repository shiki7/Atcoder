N = int(input())
C = [list(map(int, input().split())) for i in range(N)]
A = [0] * N
B = [0] * N

d = min(C[0])
for i in range(N):
    B[i] = C[0][i] - d
for i in range(N):
    A[i] = C[i][0] - B[0]

for i in range(N):
    for j in range(N):
        if A[i]+B[j] != C[i][j]:
            print("No")
            exit()

print("Yes")
print(*A)
print(*B)
