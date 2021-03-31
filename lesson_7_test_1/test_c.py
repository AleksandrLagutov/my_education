x = int(input())
top = 0
sum = 0
while x != 0:
    sum += x
    top += 1
    x = int(input())
mean = sum/top
print(round(sum/top, 2))


