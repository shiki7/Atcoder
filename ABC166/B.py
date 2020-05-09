n, k = map(int, input().split())

se = set()

for i in range(k):
    a = input()
    li = list(map(int, input().split()))
    for j in range(len(li)):
        se.add(li[j])
print(n-len(se))
