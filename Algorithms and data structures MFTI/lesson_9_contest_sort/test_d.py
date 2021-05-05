price, delta, m = map(int, input().split())
"""
Входные данные
price - цена риса
delta - на сколько увеличивается цена
m - количество недель
"""
day = 1
week = 0
outlay = 0 # Сколько потратил студент




if price >= 0 and delta >= 0 and m >= 0:
    while week < m:
        outlay += price
        day += 1
        price += delta
        if day == 8:
            week += 1
            day = 1

    print(outlay)

else:
    print(0)
