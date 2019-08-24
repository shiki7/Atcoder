# not clear
N, K = map(int, input().split())
A = list(map(int, input().split()))


def count(A: list, i):
    total = 0
    B = A*i
    for i in range(len(B)):
        for j in range(1, len(B)):
            if j <= i:
                continue
            elif B[i] > B[j]:
                total += 1
    return total


if K < 4:
    print(count(A, K))
    exit()

x2 = count(A, 2)
x3 = count(A, 3)
x4 = count(A, 4)
a = (x4-x3) - (x3-x2)
ans = a * (K-1) * (K-2)//2 + x2*(K)
print(ans % (10**9+7))
