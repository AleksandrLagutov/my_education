a = int(input())
b = int(input())
c = int(input())

def check_triangle(a,b,c):
    if a**2 == b**2 + c**2:
        return True

def cheсk_right():
    pass
def cheсk_acute():
    pass
def cheсk_obtuse():
    pass
if a < 0 or b < 0 or c < 0:
    print('impossible')
elif check_triangle(a, b, c) or check_triangle(b, c, a) or check_triangle(c, b, a):
    if cheсk_right():
        print('right')
    if cheсk_acute():
        print('acute')
    if cheсk_obtuse():
        print('obtuse')
else:
    print('impossible')



