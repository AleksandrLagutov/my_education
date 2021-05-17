original_str = list(input())
code_str = list(input())
direct_dict = dict(zip(original_str, code_str))
back_direct = dict(zip(code_str, original_str))
def convert_str(data, key_dict):
    out_list = []
    for _ in data:
        if _ in key_dict:
            out_list.append(key_dict[_])
        else:
            out_list.append(_)
    return ''.join(out_list)
first_str = list(input())
second_str = list(input())
print(convert_str(first_str, direct_dict))
print(convert_str(second_str, back_direct))