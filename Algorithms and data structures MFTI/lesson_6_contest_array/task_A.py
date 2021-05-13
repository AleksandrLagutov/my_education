input_data = (input()).split()
A = [0]*3
for i in range(3):
    A[i] = int(input_data[i])


def chek_point_on_radius(array):
    x= array[0]
    y = array[1]
    r = array[2]
    g = (x**2 + y**2)**(1/2)
    if g <= r:
        print("YES")
    else:
        print("NO")


chek_point_on_radius(A)

