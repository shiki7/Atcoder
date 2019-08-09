# -*- coding: utf-8 -*
N = int(input())
a = list(map(int, input().split()))
count = 0
while True:
	for i in range(N):
		if a[i] % 2 == 0:
			a[i] //= 2
		else:
			flag = False
			print(count)
			exit()
	count += 1
