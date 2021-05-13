with open ('data_input', 'r') as inp:
    line = inp.readline().strip()
output_line = ''
tmp = ''
range_char = '0'
for _ in line:
    if _.isalpha():
        for i in range(int(range_char)):
            output_line += tmp
        range_char = '0'
        tmp = _
    else:
        range_char += _
for i in range(int(range_char)):
    output_line += tmp
print(output_line)
with open('data_output', 'w') as out:
    out.write(output_line)
