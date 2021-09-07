from math import sqrt
import math
def validate_digit(value):
    if value.isdigit():
        print(f'''Ви ввели число - {value}''')
        return int(value)
    elif '-' in value or '.' in value or ',' in value:
        if '-' in value:
            if '.' in value or ',' in value:
                try:
                    if ',' in value:
                        value = value.replace(',', '.')
                    float(value)
                    print(f'''Ви ввели від'ємне дробове число - {value}''')
                    return float(value)
                except ValueError:
                    return False
            elif '.' not in value or ',' not in value:
                try:
                    int(value)
                    print(f'''Ви ввели від'ємне число - {value}''')
                    return int(value)
                except ValueError:
                    return False
        elif '.' in value or ',' in value:
            try:
                if ',' in value:
                    value = value.replace(',', '.')
                float(value)
                print(f'''Ви ввели дробове число - {value}''')
                return float(value)
            except ValueError:
                return False
    else:
        return False

def task_1():
    two_digigts = ('+', '-', '*', '/')
    one_digigts = ('sqr', 'sqrt')
    print('Оберіть необхідну операцію: ')
    print('1.Додавання (+)')
    print('2.Віднімання (-)')
    print('3.Множення (*)')
    print('4.Ділення (/)')
    print('5.Піднесення до квадрату (sqr)')
    print('6.Корінь квадратний (sqrt)')
    choise = input()
    if choise in two_digigts:
        number_1 = validate_digit(input('Введіть перше число: '))
        if number_1:
            number_2 = validate_digit(input('Введіть друге число: '))
            if number_2:
                if choise == '+':
                    print(f'{number_1} + {number_2} = {number_1 + number_2}')
                elif choise == '-':
                    print(f'{number_1} - {number_2} = {number_1 - number_2}')
                elif choise == '*':
                    print(f'{number_1} * {number_2} = {number_1 * number_2}')
                elif choise == '/':
                    print(f'{number_1} / {number_2} = {number_1 / number_2}')
    elif choise in one_digigts:
        number_1 = validate_digit(input('Введіть число: '))
        if number_1:
            if choise == 'sqr':
                print(f'{number_1}² = {number_1*number_1}')
            elif choise == 'sqrt':
                print(f'√{number_1} = {sqrt(number_1)}')
    else:
        print('Ви ввели не число')


def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('1. Завдання 1. Створити файл, та записати в нього текст. Підрахувати к-сть букв, слів, рядків.')
        print('2. Завдання 2. FizzBuzz.')
        print('3. Завдання 3. Конфігурації.')
        print('Будь ласка введіть номер 1 - 3, або "end" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                task_1()
            elif task == 2:
                pass
            elif task == 3:
                pass
        elif task == 'end':
            print('Завершення програми!')
            break


if __name__ == '__main__':
    main()