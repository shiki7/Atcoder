N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
li = set()
for i in range(len(ab)):
    print(sorted(ab[i]))
    li += [sorted(ab[i])]
print(li)
