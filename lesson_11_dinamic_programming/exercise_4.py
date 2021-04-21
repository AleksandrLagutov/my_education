"""
Модифицируйте алгоритм вычисления значений целевой функции так, чтобы вычислить значения prev[i], и
 восстановите траекторию наименьшей стоимости из точки 1 в точку n.
"""

N = 5
price = [0, 1, 2, 6, 2, 1]


def calculate_min_cost(n, price:list):
    C = [float('-inf'), price[1], price[1]+price[2]] + [0]*(n-2)
    prev = []
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-2], C[i-1])
        cost = i - 1 if C[i - 1] < C[i - 2] else i - 2
        prev.append(cost)
    print(prev)
    return C

def trajectory_restoration(C:list, price:list):
    prev = []
    i = len(C)
    while i > 3:
        costs = i-1 if C[i-1] < C[i-2] else i-2
        prev.append(costs)
        i = costs
    prev.append(1)
    return prev[::-1]

print(price)
cost = calculate_min_cost(N, price)
print('cost', cost[N])
print('path ',  trajectory_restoration(cost, price))
