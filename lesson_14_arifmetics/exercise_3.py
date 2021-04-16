"""
>>> forward_writing('(2−3)*(12−10)+4/2')
+∗−23−1210/42
>>> bforward_writing('(2−3)*(12−10)+4/2')
23−1210−*42/+
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
    priority = {'': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 4}
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
        else: # Если символ является бинарной операцией , тогда:

                """
                1) пока на вершине стека префиксная функция…
… ИЛИ операция на вершине стека приоритетнее o1
… ИЛИ операция на вершине стека левоассоциативная с приоритетом как у o1
… выталкиваем верхний элемент стека в выходную строку;
2) помещаем операцию o1 в стек.
                
                """
   #  Когда входная строка закончилась, выталкиваем все символы из стека в выходную строку. В стеке должны были остаться только символы операций; если это не так, значит в выражении не согласованы скобки.
def main():
    if check_brace():
        pass

if __name__ == 'main':
    main()