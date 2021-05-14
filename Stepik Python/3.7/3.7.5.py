dict_class = {str(i): [0, 0] for i in range(1, 12)}
with open('input_5', 'r') as inf:
    for line in inf:
        tmp_list = line.strip().split('\t')
        dict_class[tmp_list[0]][0] += int(tmp_list[2])
        dict_class[tmp_list[0]][1] += 1
for item, value in dict_class.items():
    print(item, (value[0]/value[1]) if value[1] > 0 else '-')