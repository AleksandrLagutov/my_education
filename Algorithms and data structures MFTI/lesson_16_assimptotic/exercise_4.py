"""
Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово входит в этот текст и вывести десять самых
 часто употребяемых слов в этом тексте и количество их употреблений.
"""
import operator
import string

input_file = open("C:\\Python26\LICENSE.txt", 'r')
file = input_file.read()
array = list(map(str, file.split()))
dictionary = dict()
for index in array:
    if index not in string.punctuation and index not in '\n':
        if index.lower() not in dictionary:
            dictionary[index.lower()] = 1
        else:
            dictionary[index.lower()] += 1
input_file.close()
dictionary = sorted(dictionary.items(), key= operator.itemgetter(1), reverse=True)
print(dictionary[:10])
#toptenwords = dict(dictionary.items()[:10])