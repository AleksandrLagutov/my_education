
"""
>>> correct_struct('///')
False
>>> correct_struct('//[]')
True
>>> correct_struct('/(([()]))/[]//')
True
>>> correct_struct('/([])/[]')
True
>>> correct_struct('(](]')
False
>>> correct_struct('(')
False
>>> correct_struct('([[[]]])')
True
>>> correct_struct(']')
False
>>> correct_struct('/')
False
>>> correct_struct('(/)/')
False
"""
import exercise_1_ariphetics as s

string = '/(([()]))/[]//'

def correct_struct(data:str):
    s.clear_steck()
    flag = True
    for char in data:
        if s.is_empty_stack() and char in ')]':
            return False
        elif char in '([' or flag is True and char in '/':
            s.push_steck(char)
            if char in '/':
                flag = False
        else:
            left_border = s.pop_steck()
            if char == ')' and left_border == '(':
                continue
            elif char == ']' and left_border == '[':
                continue
            elif char == '/' and left_border == '/':
                flag = True
                continue
            else:
                return False
    return s.is_empty_stack()

if __name__ == '__main__':
    import doctest
    doctest.testmod



