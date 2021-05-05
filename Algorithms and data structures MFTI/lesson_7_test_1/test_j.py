N = int(input())

data_list = [None]*N
for i in range(N):
    data_list[i] = [None]*3

def input_data():
    for i in range(N):
        for k in range(3):
            data_list[i][k] = int(input())
    revers_data_list = data_list[::-1]
    return revers_data_list



def search_interesting_data(data_list):
    M = int(input())
    search_list = [None]*M
    for i in range(M):
        search_list[i] = int(input())
    resalt_data = [0]*M
    for t in range(M):
        last_color = True
        for k in range(N):
            if data_list[k][0] <= search_list[t] <= data_list[k][1] and last_color:
                resalt_data[t] = data_list[k][2]
                last_color = False
    return resalt_data






if 0 <= N <= 100:
        print(*search_interesting_data(input_data()), end=' ')

