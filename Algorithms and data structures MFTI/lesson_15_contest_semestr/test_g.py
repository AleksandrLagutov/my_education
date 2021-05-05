"""
По данному числу N выведите первые N+1 строку треугольника Паскаля.

Формат входных данных
Во входных данных содержится только число N (0 < N ≤ 100).

Формат выходных данных
Выведите N + 1 строку треугольника Паскаля. Числа в строке разделяйте одним пробелом.
"""
size = int(input())

def triangle_pasc(n):
    matrix = [[0]*(n+2) for i in range(n+2)]
    matrix[1][1] = 1
    for i in range(1, n+2):
        for j in range(1, n+2):
            if i == 1 and j == 1:
                matrix[1][1] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix
tri_p =(triangle_pasc(size))
for i in  range(1, size+2):
    for j in range(1, i+1):
        print(tri_p[i-j+1][j], end=' ')
    print()