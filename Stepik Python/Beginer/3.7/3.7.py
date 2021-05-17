size_data_input = int(input())
dict_team = {}
for _ in range(size_data_input):
    len_input = input().split(';')
    for i in [0, 2]:
        if len_input[i] not in dict_team:
            dict_team[len_input[i]] = [1, 0, 0, 0, 0]
        else:
            dict_team[len_input[i]][0] += 1
    if int(len_input[1]) > int(len_input[3]):
        dict_team[len_input[0]][1] += 1
        dict_team[len_input[2]][3] += 1
        dict_team[len_input[0]][4] += 3
    elif int(len_input[1]) < int(len_input[3]):
        dict_team[len_input[2]][1] += 1
        dict_team[len_input[0]][3] += 1
        dict_team[len_input[2]][4] += 3
    elif int(len_input[1]) == int(len_input[3]):
        dict_team[len_input[0]][2] += 1
        dict_team[len_input[2]][2] += 1
        dict_team[len_input[0]][4] += 1
        dict_team[len_input[2]][4] += 1
for q, w in dict_team.items():
    print((q+':'), *w, end='\n')
