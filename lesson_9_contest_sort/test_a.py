input_data = (input()).split()
hex_a = int(input_data[0], 16)
hex_b = int(input_data[1], 16)





def convert_to_bin(num):
    base = 2
    num = int(num)
    bin = [0]*8
    top = 7
    while num > 0:
        bin[top] = num % base
        num //= base
        top -= 1
    return bin


def xor_bin(A,B):
    C = [0]*8
    for i in range(8):
        C[i] = A[i] ^ B[i]
    return C


resalt = xor_bin(convert_to_bin(hex_a),convert_to_bin(hex_b))
resalt_bin = ''.join(map(str, resalt))
resalt_hex = int(resalt_bin, 2)
print(hex(resalt_hex).lstrip("0x"))
