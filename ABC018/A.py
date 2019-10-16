a = int(input())
b = int(input())
c = int(input())
sorted_list = sorted([a, b, c], reverse=True)
for x in [a, b, c]:
    for i in range(3):
        if x == sorted_list[i]:
            print(i + 1)
            break
