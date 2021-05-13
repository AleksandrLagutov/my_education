input_data = int(input())


def convert_to_bin(num):
    base = 2
    num = int(num)
    bin = []

    while num > 0:
        bin.append(num % base)
        num //= base
    return bin


bin_array_input = convert_to_bin(input_data)
print(bin_array_input.count(1))
