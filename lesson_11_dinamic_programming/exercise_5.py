
N = 6
M = 6
ferz_pos = 0, 1
K = [[0]*(M+1) for i in range(N+1)]
K[0][0] =0
for i in range(1, N+1):
    for j in range(1, M+1):
        if K[i][j] == 0:
            K[i+1][j] =1 ; K[i][j+1] = 1; K[i+1][j+1] = 1
        elif K[i-1][j] == 1 and K[i][j-1] == 1 and K[i-1][j-1] == 1:
            K[i][j] = 0




for i in range(N):
    print(K[i])


