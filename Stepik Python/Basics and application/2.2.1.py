import simplecrypt
inf_list = []
with open('passwords.txt') as inf:
    for line in inf:
        inf_list.append(line)
print(inf_list)