x = int(input())
ans = [1]
for i in range(1, x):
    for j in range(2, x):
        if i**j > x:
            break
        else:
            ans.append(i**j)
print(max(ans))
