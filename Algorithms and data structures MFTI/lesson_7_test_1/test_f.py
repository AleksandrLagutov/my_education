A = int(input())
B = int(input())
flag = True
while flag:
    if A == B or A%B == 0:
        flag = False
    else:
        if A > B:
            A %= B
            A, B = B, A
        else:
            A, B = B, A
print(B)


