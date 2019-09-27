n, k = map(int, input().split())
l_list = map(int, input().split())
l_list = sorted(l_list, reverse=True)
print(sum(l_list[0:k]))
