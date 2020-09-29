N = int(input())
cnt = 0
for _ in range(N):
    s = input()
    if s == 'white':
        cnt += 1
if cnt > N//2:
    print('white')
else:
    print('black')
