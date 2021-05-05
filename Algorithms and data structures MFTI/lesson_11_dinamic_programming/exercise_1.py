"""
Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и +3.


"""

def numbers_of_ways(N):
    F = [0, 1, 3] + [0]*N
    for i in range(3, N+1):
        F[i] = F[i-3] + F[i - 2] + F[i - 1]
    return F[N]
print(numbers_of_ways(6))