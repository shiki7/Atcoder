from collections import defaultdict
ans = defaultdict(int)
N = int(input())

for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            ans[i*i+j*j+k*k+i*j+j*k+k*i] += 1
for i in range(N):
    print(ans[i+1])
