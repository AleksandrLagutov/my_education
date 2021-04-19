"""
forward_writing('(2−3)*(12−10)+4/2')
+∗−23−1210/42
>>> bforwaed_writing('(2-3)*(12-10)+4/2')
'23-1210-*42/+'
"""
import exercise_1_ariphetics as s


def check_brace(data:str):

    n = 0
    for i in data:
        if n < 0:
            return False
        n += 1 if i == '(' else -1
    return True if n == 0 else False

def forward_writing(data):
    s.clear_steck()



    pass


def bforwaed_writing(data):
    s.clear_steck()
    priority = {'': 0, '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 4}
    p_string = []
    for i in data:
        if i not in '(,)+,-,*,/,^':
            p_string.append(i)
        elif i == '(':
            s.push_steck(i)
        elif i == ')':
            temp = s.last_steck()
            while temp != '(':
                if not s.is_empty_stack():
                    p_string.append(s.pop_steck())
                    temp = s.last_steck()
                else:
                    return "Ошибка скобочной структуры"
            s.pop_steck()
        else:
            if not s.is_empty_stack() and priority[s.last_steck()] > priority[i]:
                while not s.is_empty_stack():
                    p_string.append(s.pop_steck())
            s.push_steck(i)
    while not s.is_empty_stack():
        p_string.append(s.pop_steck())
    result = ''.join(p_string)
    return result

def main():
    print(bforwaed_writing('(2-3)*(12-10)+4/2'))

if __name__ == '__main__':
    main()
