N = int(input())
a = list(map(int, input().split()))
print(a.index(min(max(a[:len(a)//2]), max(a[len(a)//2:])))+1)
