lens_mass = int(input())
data_mass = [None]*lens_mass
count_number = 0
for i in range(lens_mass):
    x = int(input())
    data_mass[i] = x
    this_count = data_mass.count(x)
    if this_count > count_number:
        count_number = this_count
        resalt = x
print(resalt)