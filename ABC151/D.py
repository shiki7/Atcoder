# not clear
h, w = map(int, input().split())
s = [['#'] * (w+2)]
for _ in range(h):
    s += [['#'] + list(input()) + ['#']]
s += [['#'] * (w+2)]
print(s)


def search(start, goal):
    return
