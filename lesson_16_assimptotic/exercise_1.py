"""
Допишите в следующем коде учаток функции, где repeat_count раз повторяется взятие операции pop по индексу pop_position.
Сделается чтобы если pop_position == None то брался pop() без указания индекса. Допишите код получения массивов values1,
 values2, values3. Покажите преподавателю получившиеся графики.
"""


import matplotlib.pyplot as plt
import time

def get_pop_time(size, repeat_count, pop_position=None):
    '''
    size - размер списка из нулей на котором будем тестировать скорость операции pop
    repeat_count - количество повторений для усреднения
    pop_position - позиция с которой делаем pop
    '''
    l = [0] * size
    start_time = time.time()
    #
    # code here
    #
    for i in range(size):
        if pop_position == None:
            l.pop()
        elif pop_position < size:
            l.pop(pop_position)
    end_time = time.time()
    return (end_time - start_time) / repeat_count

repeat_count = 1000
values1 = [get_pop_time(size,repeat_count) for size in range(10, 1000)]
values2 = [get_pop_time(size,repeat_count,0) for size in range(10, 1000)]
values3 = [get_pop_time(size,repeat_count,size) for size in range(10, 1000)]

plt.plot(values1, label='Pop no args')
plt.plot(values2, label='Pop start list')
plt.plot(values3, label='Pop end list')
plt.ylabel('pop time')
ax = plt.subplot(111)
ax.legend()
plt.show()