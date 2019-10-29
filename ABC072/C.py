import collections

n = int(input())
a = list(map(int, input().split()))
counter = collections.Counter(a)
max_count = 0
for i in range(0, max(a) + 1):
    max_count = max(max_count, counter[i - 1] + counter[i] + counter[i + 1])
print(max_count)
