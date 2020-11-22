N = int(input())
S = [input() for _ in range(N)]
dow = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(N):
    for j in range(len(dow)):
        if S[i] == dow[j]:
            print(dow[(j + 1) % 7])
