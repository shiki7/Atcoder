A = input()
B = input()
C = input()

cur = A[0]
A = A[1:]
for _ in range(len(A)+len(B)+len(C)):
    if cur == 'a':
        if len(A) == 0:
            print('A')
            exit()
        cur = A[0]
        A = A[1:]
    elif cur == 'b':
        if len(B) == 0:
            print('B')
            exit()
        cur = B[0]
        B = B[1:]
    elif cur == 'c':
        if len(C) == 0:
            print('C')
            exit()
        cur = C[0]
        C = C[1:]
