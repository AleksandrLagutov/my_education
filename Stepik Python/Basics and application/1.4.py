"""
Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания
 пространств имен и добавление в них переменных.
"""
def add(name, var):
    variables[name].add(var)

def create(name, parent):
    if name not in namespaces:
        namespaces[name] = [parent]
    else:
        namespaces[name].append(parent)
    variables[parent] = set()
    pass
def get(name, var):
    if var in variables[name]:
        return name
    else:
        for k in namespaces:
            for v in namespaces[k]:
                if name == v:
                    return get(k, var)
    pass
list_line = []
with open('input_1.4', 'r') as inf:
    for line in inf:
        list_line.append(line.strip())


namespaces = {'global': [None]}
variables = {'global': set()}
#sise_input = int(input())
for _ in list_line:
    cmd, namespace, variable = (str(i) for i in _.split())
    if cmd == 'create':
        create(variable, namespace)
    elif cmd == 'add':
        add(namespace, variable)
    elif cmd == 'get':
        print(get(namespace, variable))
