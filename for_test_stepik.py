with open ('data_input', 'r') as inp:
    line = inp.readline().strip()
output_line = []
tmp = ''
range_char = ''
for _ in line:
    if _.isalpha():
        tmp = _
    if _.isalnum():
        range_char += _

