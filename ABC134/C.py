N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
max_A = max(A)
max_num = 0
for i in range(N):
    if A[i] == max_A:
        # 最大値が複数ある場合の計算削減
        max_num += 1
        if max_num > 1:
            print(max_A)
        else:
            print(max(A[:i] + A[i + 1:]))
    else:
        print(max_A)
