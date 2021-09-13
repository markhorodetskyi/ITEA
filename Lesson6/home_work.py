import random
from random import choice
from math import sqrt


def validate_digit():
    loop = True
    while loop:
        value = input()
        if value.isdigit():
            print(f'''Ви ввели число - {value}''')
            return int(value)
        elif '-' in value or '.' in value or ',' in value:
            if '-' in value:
                if '.' in value or ',' in value:
                    try:
                        if ',' in value:
                            value = value.replace(',', '.')
                        print(f'''Ви ввели від'ємне дробове число - {value}''')
                        return float(value)
                    except ValueError:
                        print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                        continue
                elif '.' not in value or ',' not in value:
                    try:
                        print(f'''Ви ввели від'ємне число - {value}''')
                        return int(value)
                    except ValueError:
                        print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                        continue
            elif '.' in value or ',' in value:
                try:
                    if ',' in value:
                        value = value.replace(',', '.')
                    print(f'''Ви ввели дробове число - {value}''')
                    return float(value)
                except ValueError:
                    print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                    continue
        else:
            print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
            continue


def task_1():
    two_digigts = ('1', '2', '3', '4', '+', '-', '*', '/')
    one_digigts = ('5', '6', 'sqr', 'sqrt')
    print('Оберіть необхідну операцію: ')
    print('1.Додавання (+)')
    print('2.Віднімання (-)')
    print('3.Множення (*)')
    print('4.Ділення (/)')
    print('5.Піднесення до квадрату (sqr)')
    print('6.Корінь квадратний (sqrt)')
    choise = input()
    if choise in two_digigts:
        print('Введіть перше число:')
        number_1 = validate_digit()
        if number_1:
            print('Введіть друге число:')
            number_2 = validate_digit()
            if number_2:
                if choise == '+' or choise == '1':
                    print(f'{number_1} + {number_2} = {number_1 + number_2}')
                elif choise == '-' or choise == '2':
                    print(f'{number_1} - {number_2} = {number_1 - number_2}')
                elif choise == '*' or choise == '3':
                    print(f'{number_1} * {number_2} = {number_1 * number_2}')
                elif choise == '/' or choise == '4':
                    print(f'{number_1} / {number_2} = {number_1 / number_2}')
    elif choise in one_digigts:
        number_1 = validate_digit()
        if number_1:
            if choise == 'sqr' or choise == '5':
                print(f'{number_1}² = {number_1*number_1}')
            elif choise == 'sqrt' or choise == '6':
                print(f'√{number_1} = {sqrt(number_1)}')
    else:
        print('Ви ввели не число')


def dict_generator():  # Випадково генерує словник з двох даних списків.
    digit = [1, 2, 3, 4, 5]
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    keys = [digit, words]
    my_dict = {}
    for i in range(0, 4):
        my_dict.update({choice(choice(keys)): choice(choice(keys))})
    return my_dict


def task_2():
    my_dict = dict_generator()
    key_list = [key for key in my_dict.keys() if 'str' in str(type(key))]
    print(f'Згенеровано словник - {my_dict}')
    print(f'Згенеровано з стрічковими ключами - {key_list}')


def task_3():
    with open('Text', 'r', encoding='utf-8') as file:
        text = file.read()
        if text:
            text = text.replace('\n', ' ').replace('.\n', '. ')
            text = text.split('. ')
            new_text = ''
            for sentence in range(len(text)):
                new_text = f'{new_text} {text[sentence].capitalize()}.'
            with open('Text', 'w', encoding='utf-8') as new_text_file:
                new_text_file.write(new_text)
            print(new_text)
            print(f'У тексті знайдено {len(text)} речень. Всі речення тепер з великої букви.')
        else:
            print('Файл порожній')


def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('1. Завдання 1. Калькулятор.')
        print('2. Завдання 2. String keys.')
        print('3. Завдання 3. Підрахунок речень.')
        print('Будь ласка введіть номер 1 - 3, або "end(enter)" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                task_1()
            elif task == 2:
                task_2()
            elif task == 3:
                task_3()
        elif task == 'end' or task == '':
            print('Завершення програми!')
            break


if __name__ == '__main__':
    main()
