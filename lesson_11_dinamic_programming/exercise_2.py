"""
Решите задачу о количестве способов достичь точки n из точки 1, если кузнечик умеет прыгать +1, +2 и *3.
"""

def numbers_of_ways(N):
    F = [0, 1] + [0]*N
    for i in range(2 ,N+1):
        triple_jump = 1 if i%3 == 0 else 0
        F[i] = F[i-2] + F[i-1] + triple_jump
    return F[N]
print(numbers_of_ways(9))