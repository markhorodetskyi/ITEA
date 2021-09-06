from random import randint, choice
from string import ascii_lowercase


def yes_or_no():
    print('Введіть "так"(т) або "ні"(н): ')
    loop = True
    while loop:
        choise = input()
        choise = choise.lower()
        if choise == 'так' or choise == 'т':
            return True
        elif choise == 'ні' or choise == 'н':
            return False
        else:
            print('Не коректна відповідь. Введіть "так"(т) або "ні"(н): ')


def task_1():
    print(f'Згенерувати випадковий набір букв побудованих у вигляді слів з пробілами та переходом на новий рядок для '
          f'демонстрації підрахунку слів? У випадку негативної відповіді буде використано сталий текст.')
    if yes_or_no():
        with open('home_work_file', 'w') as file:  # Блок генерує випадковий набір букв побудованих у вигляді слів з пробілами та переходом на новий рядок для демонстрації підрахунку слів.
            alphabet = ascii_lowercase
            text = ''
            ent_space = (' ', ' ', ' ', '\n')  # Список для виподкової генерації рядка. Три пробіли для того, щоб з меншити ймовірність попадання на '\n'
            for words in range(1, 200):
                word = ''
                for letter in range(0, randint(4, 12)):
                    word += choice(alphabet)
                word += choice(ent_space)
                text += word
            file.write(text)
            word += choice(ent_space)
    else:
        with open('text', 'r') as text:
            with open('home_work_file', 'w') as file:
                file.write(text.read())

    with open('home_work_file', 'r') as file:
        text = file.readlines()
        word_count = 0
        letter_count = 0
        for row in text:
            words = row.split(' ')
            for word in words:
                word_count += 1
                letter_count += len(word)
        print(f'К-сть рядків - {len(text)}')
        print(f'К-сть слів - {word_count}')
        print(f'К-сть букв - {letter_count}')


def task_2():
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(f'Число з списку = {i}')


def build_config_dict(file_path):
    with open(str(file_path), 'r') as file:
        config_dict = {}
        config = file.readlines()
        for row in config:
            space = row.find(' ')
            parameters = row[:space]
            if parameters:
                config_dict[str(parameters)] = row[space:]
        return config_dict


def write_to_file(file_path, config_dict):
    with open(str(file_path), 'w') as file:
        text = ''
        for option, value in config_dict.items():
            text += option + ' ' + value
        file.write(text)
        print('Новий вигляд конфігураційного файлу: ')
        print(text)


def task_3():
    while True:
        print('')
        print('-----------------')
        config_dict = build_config_dict('config')
        print('Доступні опції: ')
        for option in config_dict.keys():
            print('    '+option)
        print('Введіть опцію, яку ви хочете змінити або end(e) для поверення в попереднє меню: ')
        option = input()
        if option in config_dict.keys():
            print(f'Введіть нове значення для опції - {option}')
            config_dict[option] = input()+';\n'
        elif option == 'end' or option == 'e':
            break
        else:
            print(f'Опції - {option}, немає у файлі конфігурації')
        write_to_file('config', config_dict)
        print('-----------------')


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
                task_2()
            elif task == 3:
                task_3()
        elif task == 'end':
            print('Завершення програми!')
            break


if __name__ == '__main__':
    main()
