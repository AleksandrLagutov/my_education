x = int(input())
index = 0
A = [0, 0, 1]
flag = True
while flag:
    i = len(A)
    for k in range(i):
        if A[k] > x:
            print(k)
            flag = False
    A.append(A[i-3] + A[i-2] + A[i-1])


