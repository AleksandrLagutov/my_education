"""
Сколько раз цифра d входит в десятичную запись числа n?
Входные данные
Число 0≤d≤9. Пробел. Целое положительное число n в десятичной системе (0 ≤ n ≤ 3·10 6) .В задании ошибка,
 так как в тесте дают чсло порядка 10^7
Выходные данные
Сколько раз цифра d входит в запись числа n.
"""
number_d, number_n = map(int, input().split())
if 0 <= number_d <= 9 and 0 <= number_n <= 3*(10**7):
    how_many_t = 0
    while number_n > 0:
        how_many_t += 1 if number_n % 10 == number_d else 0
        number_n //= 10
    print(how_many_t)

else:
    print(0)
