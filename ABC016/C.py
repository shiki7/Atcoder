n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
for i in range(1, n+1):
    friends = []
    for a, b in ab:
        if a == i:
            friends.append(b)
        elif b == i:
            friends.append(a)
    friends_of_friends = []
    for a, b in ab:
        if (a in friends and b != i and b not in friends):
            friends_of_friends.append(b)
        if (b in friends and a != i and a not in friends):
            friends_of_friends.append(a)
    print(len(list(set(friends_of_friends))))
