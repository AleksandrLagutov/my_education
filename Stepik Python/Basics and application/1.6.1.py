"""
lst_mro = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

lst_q = [  # список введённых запросов
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]
"""
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return None
    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None
graf = {}
lst_mro = []
lst_q = []
n = int(input())
for _ in range(n):
    lst_mro.append(input())
q = int(input())
for _ in range(q):
    lst_q.append(input())

for _ in lst_mro:
    a, *b = _.replace(":", "").split()
    if a not in graf:
        graf[a] = b
for _ in lst_q:
    start, end = _.split()
    if find_path(graf,end,start):
        print('Yes')
    else:
        print('No')