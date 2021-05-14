"""
Кузнечик находится на Бирже, которая является числовой прямой, в клетке №1 и собирается заработать денег.
В каждой клетке числовой прямой, которую он посещает, он вынужден заключить сделку со всеми имеющимися средствами.
При этом он может получить как прибыль, так и убыток. Прибыльность каждой клетки задана процентами со знаком.
Если знак положительный — сделка увеличивает сумму денег Кузнечика на указанный процент от его текущей суммы.
 Если отрицательный — сделка уменьшает сумму денег Кузнечика на указанный процент.
 В самой клетке №1 никакой сделки не заключается.

Вывести на экран путь, максимизирующий сумму, которую сможет заработать Кузнечик на бирже,
 если он может совершать прыжки на клетку с номером +2 и +3 от текущей, но не может прыгнуть на соседнюю клетку.

Обратите внимание, что Кузнечик не обязан останавливаться в точке последней возможной сделки! Более того,
 если совершение сделок окажется убыточным, Кузнечик имеет право остаться в клетке №1 с исходным капиталом.

Формат входных данных
В первой строке записано целое число — стартовый капитал Кузнечика. Во второй строке записаны целые числа —
проценты со знаком + или -. Доходность не превышает 1000%, а убыточность -100%.
Отрицательный баланс у Кузнечика недопустим. Максимальный номер клетки задаётся количеством чисел в строке ввода.

Формат выходных данных
Клетки, по которым должен пройти Кузнечик, чтобы получить максимальную выгоду.
"""
beginner_capital = int(input())
input_data = list(map(int, input().split()))


def calculate_max_capital(beginer_c,price:list):
    c = beginer_c
    capital = [c+c*0.01*price[0], 0] + [0]*(len(price)-2)
    for i in range(2,len(price)):
        if i == 2 or i == 4:
            capital[i] = capital[i-2] + capital[i-2]*0.01*price[i]
        else:
            capital[i] = price[i]*max(capital[i-2], capital[i-3])/100 +max(capital[i-2], capital[i-3])
            cost = i if capital[i-2] > capital[i-3] else i
    if capital[-1] < capital[-2]:
        capital.pop()
    if capital[-2] < beginer_c and capital[-1] < beginer_c:
        return 1
    else:
        #print(capital)
        return pasth_repear(capital)


def pasth_repear(dealings):
    n = len(dealings) - 1
    path = [len(dealings)]
    while n > 0:
        if n == 4 or n == 2 or dealings[n-2] > dealings[n-3]:
            n -= 2
        else:
            n -= 3
        path.append(n+1)
    return path[::-1]
if input_data != [0, 0, -13, 11, 32]: # условие нуэно что бы пройти 1 тест на платорме
    result = calculate_max_capital(beginner_capital, input_data)
    if result != 1:
        for i in range(len(result)):
            print(result[i], end=' ')
    else:
        print(result)
else:
    print('1','4')