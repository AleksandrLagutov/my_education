x= int(input())
max_even = 0

while x != 0:
    if x%2 == 0 and x > max_even:
        max_even = x
    x = int(input())
print(max_even)
