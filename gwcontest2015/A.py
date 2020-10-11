a = [25, 39, 51, 76, 163, 111, 128, 133, 138]
b = set([0])
for i in a:
    tmp = set([])
    for j in b:
        tmp.add(j)
        tmp.add(i+j)
    b = tmp
ans = set([])
for i in b:
    ans.add(i)
    ans.add(i+58)
    ans.add(i+136)
ans = sorted(list(ans))
for i in range(len(ans)):
    print(ans[i])
