A = [0]*3
for i in range(3):
    A[i] = int(input())
A = sorted(A, reverse=True)


def checktriangle(mass: list):
    flag = False
    for i in range(3):
        if mass[i] < 0:
            return False
    for i in range(3):
        lock_mass = [0] * 3
        for k in range(3):
            lock_mass[k] = mass[k]
        lock_mass.pop(i)
        if mass[i] < sum(lock_mass):
            flag = True
        else:
            return False
    return flag


if checktriangle(A):
    if A[0]**2 == A[1]**2 + A[2]**2:
        print('right')
    if A[0]**2 < A[1]**2 + A[2]**2:
        print('acute')
    if A[0]**2 > A[1]**2 + A[2]**2:
        print('obtuse')
else:
    print('impossible')



