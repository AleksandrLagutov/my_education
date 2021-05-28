inp_data = list(map(int, input("Input data\n").split()))
if len(inp_data) != 0:
    mean = sum(inp_data)/len(inp_data)
    tmp = 0
    for i in inp_data:
        tmp += (i - mean)**2
    disp = tmp/(len(inp_data)-1)
    SP = disp**0.5
    print(SP)
else:
    print("Ziro data")
