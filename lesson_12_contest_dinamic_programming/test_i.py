"""
Написать функцию make_exchange(money, coins), которая принимает сумму денег (целое число) и массив номиналов разменных монет (целых чисел) (возможно пустой) и возвращает количество способов произвести размен. Считаем, что разменных монет бесконечное множество.

Формат выходных данных
Число способов произвести размен. Способы 1+2 и 2+1 считаем тождественными.
"""
def make_exchange(money:int, coins:list):
    count = [0]*(money+1)
    count[0] = 1
    if money < 0 or len(coins) == 0:
        return 0
    for i in range(len(coins)):
        for j in range(money+1):
            if j >= coins[i]:
                count[j] += count[j-coins[i]]
    return count[money]


print(make_exchange(1, [2, 1]))


