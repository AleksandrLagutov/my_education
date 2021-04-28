"""
Дан словарь task4/en-ru.txt с однозначным соответствием английских и русских слов в таком формате:
cat - кошка

dog - собака

mouse - мышь

house - дом

eats - ест

in - в

too - тоже
Здесь английское и русское слово разделены двумя табуляциями и минусом: '\t-\t'.
В файле task4/input.txt дан текст для перевода, например:
Mouse in house. Cat in house.
Cat eats mouse in dog house.
Dog eats mouse too.
Требуется сделать подстрочный перевод с помощью имеющегося словаря и вывести результат в output.txt. Незнакомые словарю
слова нужно оставлять в исходном виде.
"""
lint = []
with open("en-ru", 'r', encoding='utf8', ) as dictionary:
    data = dictionary.read()
    data_2 = data.split('\n')
    line = dict([i for i in t.split('\t-\t')] for t in data_2)

with open("input", 'r', encoding='utf8') as sometext:
    for lines in sometext:
        stroka = lines.split()
        for world in stroka:
           if line.get(world.lower().strip(',.')) != None:
               print(line[world.lower().strip(',.')], end=' ')
           else:
               print(world, end=' ')
        print()



#print(line['cat'])