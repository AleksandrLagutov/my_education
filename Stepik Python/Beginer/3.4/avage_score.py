avenge_of_subject = [0 for i in range(3)]
avenge_result_students = []
count_of_students = 1
with open('data_input', 'r') as inp:
    for line in inp:
        count_of_students += 1
        line = line.split(';')
        for i in range(3):
            avenge_of_subject[i] += int(line[i+1])
        avenge_result_students.append(sum(int(i)/3 for i in line[1:]))
for _ in range(3):
    avenge_of_subject[_] = str(avenge_of_subject[_] / (count_of_students - 1))
avenge_of_subject_str = ' '.join(avenge_of_subject)
print(avenge_of_subject_str)

with open('data_output', 'w') as outp:
    for _ in range(count_of_students-1):
        outp.write(str(avenge_result_students[_]) + '\n')
    outp.write(avenge_of_subject_str)