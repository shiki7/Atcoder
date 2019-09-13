N, M = map(int, input().split())
py = [list(map(int, input().split())) for _ in range(M)]
pyi = []
for i, x in enumerate(py):
    x.append(i)
    pyi.append(x)
pyi.sort()

dic = {}
number_list = []
for p, y, i in pyi:
    w = ''
    w = "0" * (6 - len(str(p))) + str(p)

    if p in dic:
        dic[p] += 1
    else:
        dic[p] = 1
    w += "0" * (6 - len(str(dic[p]))) + str(dic[p])
    number_list.append([i, w])
number_list.sort()
for i in range(len(number_list)):
    print(number_list[i][1])
