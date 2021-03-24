N = int(input())
A = [0]*N
L = 0
L_max = 1
if N == 0:
    L_max = 0
else:
    for i in range(N):
        A[i] = int(input())
        if A[i] == 1:
            L += 1
        else:
            L = 0
        if L > L_max:
            L_max = L
print(L_max)
