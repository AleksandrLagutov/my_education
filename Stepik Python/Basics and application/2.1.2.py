
lst_mro = [  # список введённых строк
    'ArithmeticError',
    'ZeroDivisionError : ArithmeticError',
    'OSError',
    'FileNotFoundError : OSError'
]

lst_q = [  # список введённых запросов
    'ZeroDivisionError'
    'OSError',
    'ArithmeticError',
    'FileNotFoundErrorующий класс'
]

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
"""
lst_mro = []
lst_q = []
n = int(input())
for _ in range(n):
    lst_mro.append(input())
q = int(input())
for _ in range(q):
    lst_q.append(input())
"""
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