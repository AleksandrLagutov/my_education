
def dot_product(N, vector1, vector2):
    summ = 0
    for i in range(N):
        summ += vector1[i]*vector2[i]
    return summ
