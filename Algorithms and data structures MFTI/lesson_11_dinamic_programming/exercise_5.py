
N = 6
M = 10
K = [[0]*(M) for i in range(N)]
K[0][0] = 0
for i in range(0, N):
    for j in range(0, M):
        test = K[i][j]
        if K[i][j] == 0:
            for k in range(i+1, N):
                K[k][j] = 1
                for t in range(j+1, M):
                    K[i][t] = 1
                    if abs(i - k) == abs(j - t):
                        K[k][t] = 1

for i in range(N):
    print(K[i])


