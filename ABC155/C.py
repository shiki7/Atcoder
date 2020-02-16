from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

counter = Counter(s)
index = 0
ans = []
for k, v in counter.most_common():
    if index == 0:
        max_v = v
        ans.append(k)
    else:
        if v == max_v:
            ans.append(k)
        else:
            break
    index += 1
ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])
