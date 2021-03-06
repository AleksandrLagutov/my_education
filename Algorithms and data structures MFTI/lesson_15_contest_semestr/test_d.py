"""
В одном государстве произошла реформа избирательной системы. С момента ее введения все избиратели государства делятся на
K, возможно не равных по объему, групп. Внутри каждой группы проходит голосования "за" или "против".
Если больше половины группы проголосовала "за", то общий голос группы считался "за", иначе - "против".
Любой вопрос решался положительно, если больше половины групп проголосовало "за". Все бы ничего, но в такой системе
есть недостаток. Партия, устроившая такую систему, получила возможность решать вопросы в свою пользу. Для этого они
поместили в группы своих стронников. Например, для групп численностью 5, 5 и 7 человек достаточно иметь по три своих
 человека в первых двух группах. Всего 6 человек смогут решить вопрос в пользу партии. От Вас потребуется посчитать,
какое минимальное количество сторонников надо иметь партии для заданного разбиения на группы.

Формат входных данных
На первой строке дано натуральное число K ≤ 10000. На следующей строке вводится K натуральных чисел через пробел.

Формат выходных данных
Одно число — минимальное количество сторонников партии.
"""


def half_vaits(number):
    return number // 2 + 1


groups = int(input())
count_supp = 0
data = list(map(int,input().split()))
sort_data = sorted(data)
short_data = sort_data[:half_vaits(groups)]
for i in short_data:
    count_supp += half_vaits(i)
print(count_supp)


