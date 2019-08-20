# -*- coding: utf-8 -*-
# not clear
s = list(input())
t = list(input())
s_counter = {}
t_counter = {}
for key in s:
    if key in s_counter:
        s_counter[key] += 1
    else:
        s_counter[key] = 1

for key in t:
    if key in t_counter:
        t_counter[key] += 1
    else:
        t_counter[key] = 1
print(s_counter)
print(t_counter)

counter = []
for k, v in t_counter.items():
    if s_counter[k] != None:
        counter.append(v / s_counter[k])
max_count = max(counter)
max_index = counter.index(max_count)
print(max_index + max_count*(len(s)))
