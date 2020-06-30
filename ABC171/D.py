import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

cnt_list = collections.Counter(A)
total = sum(A)
for i in range(Q):
    cnt_list[BC[i][1]] += cnt_list[BC[i][0]]
    total += (BC[i][1] - BC[i][0]) * cnt_list[BC[i][0]]
    cnt_list[BC[i][0]] = 0
    print(total)
