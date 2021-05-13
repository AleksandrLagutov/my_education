input_data = (input()).split()
A = [0]*3
if int(input_data[0]) != 0:
    for i in range(3):
        A[i] = int(input_data[i])


def calculation_of_contribution(A):
    deposit = A[0]
    percent = A[1]
    reach_deposit = A[2]
    years = 0
    while deposit < reach_deposit:
        years += 1
        years_percent = (deposit / 100) * percent
        deposit += years_percent
        deposit = int(deposit*100)/100
    return years


if input_data[0] == 0:
    print(0)
else:
    print(calculation_of_contribution(A))


