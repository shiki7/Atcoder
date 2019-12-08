import itertools


def xORSum(arr, n):
    ans = 0
    for i in range(0, n):
        zc = 0
        oc = 0
        idsum = 0
        for j in range(i, n):
            if (arr[j] % 2 == 0):
                zc = zc + 1

            else:
                oc = oc + 1
            arr[j] = int(arr[j] / 2)

        idsum = oc * zc * (1 << i)
        ans = ans + idsum
    return ans


n = int(input())
a = list(map(int, input().split()))

print(xORSum(a, n) % (10**9+7))
