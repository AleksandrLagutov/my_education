"""
Реализовать стековый калькулятор на python. Написать программу, которая читает выражение в обратной польской нотации и
считает его значение или пишет, что выражение составлено не корректно (если оно некорректно).
Считает только до 10!!
23-15-*42/+
123^+2*
>>> steck_colculate('123^+2*')
18
"""

import exercise_3 as p
import exercise_1_ariphetics as s



def steck_colculate(char):
    tmp = 0
    s.clear_steck()
    for i in char:
        if i in '0123456789':
            s.push_steck(i)
        else:
            oper_2 = int(s.pop_steck())
            oper_1 = int(s.pop_steck())
            if i == '+':
                tmp = oper_1 + oper_2
            elif i == '-':
                tmp = oper_1 - oper_2
            elif i == '*':
                tmp = oper_1 * oper_2
            elif i == '/':
                tmp = oper_1 / oper_2
            elif i == '^':
                tmp = oper_1 ** oper_2
            s.push_steck(tmp)
    return s.last_steck()


def main():
    print(p.bforwaed_writing('(2-3)*(1-5)+4/2'))
    print(steck_colculate(p.bforwaed_writing('(2-3)*(1-5)+4/2')))


if __name__ == '__main':
    main()
