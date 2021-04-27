"""
Вывести на экран все элементы множества A, которых нет в множестве B.

A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
for x in A:
    ...
"""
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
for x in A:
    print(x if x not in B else '', end='')
