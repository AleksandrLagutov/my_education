B = []
x = int(input())
max_namber = 0
while x !=0:
    B.append(x)
    if len(B) == 6:
        if B[0] > max_namber:
            max_namber = B[0]
        B.pop(0)
    x = int(input())
print(max_namber)

