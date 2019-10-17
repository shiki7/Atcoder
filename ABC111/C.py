import collections

n = int(input())
v = list(map(int, input().split()))
even = []
odd = []
for i in range(0, n, 2):
    odd.append(v[i])
for i in range(1, n, 2):
    even.append(v[i])
odd_counter = collections.Counter(odd)
even_counter = collections.Counter(even)

odd_counter_sorted = sorted(odd_counter.items(),
                            key=lambda x: x[1],
                            reverse=True)
even_counter_sorted = sorted(even_counter.items(),
                             key=lambda x: x[1],
                             reverse=True)
if odd_counter_sorted[0][0] != even_counter_sorted[0][0]:
    print(
        len(odd) - odd_counter_sorted[0][1] + len(even) -
        even_counter_sorted[0][1])
else:
    ans = float("inf")
    if len(odd_counter_sorted) > 1:
        a = len(odd) - odd_counter_sorted[1][1] + len(
            even) - even_counter_sorted[0][1]
    else:
        a = len(odd) + len(even) - even_counter_sorted[0][1]

    if len(even_counter_sorted) > 1:
        b = len(odd) - odd_counter_sorted[0][1] + len(
            even) - even_counter_sorted[1][1]
    else:
        b = len(odd) - odd_counter_sorted[0][1] + len(even)
    print(min(a, b))
