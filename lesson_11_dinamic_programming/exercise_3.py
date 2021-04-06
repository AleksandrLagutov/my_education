"""
Напишите функцию calculate_min_cost(n, price) вычисления наименьшей стоимость достижения клетки n из клетки 1
"""
N = 3
price = [i for i in range(N+1)]


def calculate_min_cost(n, price:list):
    C = [float('-inf'), price[1], price[1]+price[2]] + [0]*(n-2)
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-2], C[i-1])
    return C[n]

print(price)
print(calculate_min_cost(N, price))
