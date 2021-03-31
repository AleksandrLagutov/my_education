
B = [0]*3
top = 0
summ = 0
max = 0
min = None
mod = 0
i=0

def vich(C):
    global summ, min, max, mod

    for i in range(3):
        summ += C[i]
        if min == None:
            min = C[i]
        elif C[i] < min:
            min = C[i]
        if C[i] > max:
            max = C[i]
    mod += (C[0] + C[1] + C[2]) % C[2]

def chek(x):
    if len(x)>3:
        return False
    for i in range(len(x)):
        if x[i] == ' ':
            return False
    else:
        return True







x = input()
if chek(x):

    while x != '#':
        B[i] = int(x)
        i += 1
        top += 1
        if i == 3:
            vich(B)
            i = 0
        x = input()


    mean = summ / top
    print(round(mean, 3), max, min, mod)
else:
    input_data = x.split()
    N = len(input_data)
    A = [0]*N
    tmp = int(input_data[0])
    for i in range(0, N-1, 1):
        A[i] = int(input_data[i+1])
    A[N-1] = tmp
    for i in range(N):
        print(A[i], end=' ')




