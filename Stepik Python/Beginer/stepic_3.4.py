dict_char = {}
with open('data_ input_2', 'r') as inp:
    for line in inp:
        tmp = line.strip()
        for i in tmp.split():
            if i.lower() not in dict_char:
                dict_char[i.lower()] = 1
            else:
                dict_char[i.lower()] += 1
maximum = max(dict_char, key=dict_char.get)
print(maximum, dict_char[maximum])
#sorted_dict = sorted(dict_char, key=dict_char.__getitem__)
#print(sorted_dict[-1], dict_char[sorted_dict[-1]])