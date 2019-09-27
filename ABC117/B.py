n = int(input())
leng = list(map(int, input().split()))
leng.sort()
if leng[-1] < sum(leng[0:n - 1]):
    print('Yes')
else:
    print('No')
