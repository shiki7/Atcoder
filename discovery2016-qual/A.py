import math
s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
n = int(input())
m = math.ceil(len(s) / n)
for i in range(m):
    print(s[n*i:n*(i+1)])
