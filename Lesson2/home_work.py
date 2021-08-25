import random
import time


def is_float(value):
    try:
        if ',' in value:
            value = value.replace(',', '.')
        float(value)
        return value
    except ValueError:
        return False
    except Exception as e:
        print(f'Error: {e}')
        return False


def yes_or_no():
    print('Введіть "так" або "ні": ')
    loop = True
    while loop:
        choise = input()
        choise = choise.lower()
        if choise == 'так':
            return True
        elif choise == 'ні':
            return False
        else:
            print('Не коректна відповідь. Введіть "так" або "ні": ')


def check_value(value):
    if value:
        if is_float(value):
            value = is_float(value)
            if value.isdigit():
                print(f'Ви ввели число - {value}')
                return int(value)
            else:
                if int(float(value)) < 0:
                    print(f'''{value} - є від'ємним числом. Прибрати знак мінус?.''')
                    if yes_or_no():
                        value = value[1:]
                    else:
                        return False
                if value.isdigit():
                    print(f'Ви ввели число - {value}')
                    return int(value)
                else:
                    print(f'{value} - є дробовим числом. Конвертувати в натуральне число?')
                    if yes_or_no():
                        value = int(float(value))
                        print(f'Ви ввели число - {value}')
                        return value
                    else:
                        return False
        else:
            print(f'{value} - не схоже на число. Спробуйте ще раз.')
            return False
    else:
        print('Ви нічого не ввели. Спробуйте ще раз.')
        return False


def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('Будь ласка введіть номер завдання 1-5, або "end" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                print('Завдання 1. Виводить надрукований користувачем текст та к-сть символів.')
                loop = True
                while loop:
                    text = input('Будь ласка введіть що-небудь: ')
                    if text:
                        print(f'    Ви ввели: "{text}". К-сть символів - {len(text)}')
                        loop = False
                    else:
                        print('Ви нічого не ввели. Спробуйте ще раз.')

            elif task == 2:
                print('Завдання 2. Виводить результат суми, різниці і діленя двох натуральних чисел введених '
                      'користувачем. А також квадрат першого числа.')
                loop_one = True
                while loop_one:
                    digits_one = input('Будь ласка введіть перше число:')
                    digits_one = check_value(digits_one)
                    if digits_one:
                        loop_two = True
                        while loop_two:
                            digits_two = input('Будь ласка введіть друге число:')
                            digits_two = check_value(digits_two)
                            if digits_two:
                                print(f'    Сума двох чисел: {digits_one} + {digits_two} = {digits_one + digits_two}.')
                                print(
                                    f'    Різниця двох чисел: {digits_one} - {digits_two} = {digits_one - digits_two}.')
                                print(
                                    f'    Ділення двох чисел: {digits_one} / {digits_two} = {digits_one / digits_two}.')
                                print(f'    Квадрат першого числа {digits_one}:  {digits_one ** 2}.')
                                loop_two = False
                                loop_one = False

            elif task == 3:
                print('Завдання 3. Вираховує к-сть шматків піц на одну людину.')
                loop_one = True
                while loop_one:
                    print('Будь ласка введіть к-сть людей: ')
                    people = input()
                    people = check_value(people)
                    if people:
                        loop_two = True
                        while loop_two:
                            print('Будь ласка введіть к-сть pizza: ')
                            pizza = input()
                            pizza = check_value(pizza)
                            if pizza:
                                pieces = pizza * 8
                                residual = pieces % people
                                each_one_piece = int((pieces - residual) / people)
                                if people == 1:
                                    human = 'людина'
                                else:
                                    human = 'людей'
                                if pizza == 1:
                                    pizzas = 'піцою'
                                else:
                                    pizzas = 'піцами'
                                if each_one_piece == 1:
                                    count = 'шматку'
                                else:
                                    count = 'шматки'
                                print(f'    {people} {human} з {pizza} {pizzas}')
                                if people == 1:
                                    print(f'    Всі {each_one_piece} шматки одній людині')
                                else:
                                    print(f'    Кожному по {each_one_piece} {count}')
                                if residual == 0:
                                    print(f'    Зайвих шматків немає')
                                elif residual == 1:
                                    print(f'    {people} {human} будуть боротись за останній шматок')
                                elif residual <= 4:
                                    print(f'    {people} {human} будуть боротись за останні {residual} шматки')
                                else:
                                    print(f'    {people} {human} будуть боротись за останні {residual} шматків')
                                loop_two = False
                                loop_one = False
            elif task == 4:
                print('Завдання 4. Конвертер валют.')
                currencies = {1: {'name': 'USD', 'points': 1},
                              2: {'name': 'EUR', 'points': 1.17165},
                              3: {'name': 'GBP', 'points': 1.37660},
                              4: {'name': 'UAH', 'points': 0.0363}}
                print('Доступні валюти: ')
                for number in currencies.keys():
                    print(f'''{number}: {currencies[number]['name']}''')
                print('Введіть номер валюти яку Ви хочете порівняти: ')
                loop_one = True
                while loop_one:
                    first_curr = input()
                    first_curr = check_value(first_curr)
                    if first_curr:
                        if first_curr <= 4:
                            loop_two = True
                            while loop_two:
                                print(
                                    f'''Введіть номер валюти з якою ви хочете порівняти {currencies[first_curr]['name']}: ''')
                                second_curr = input()
                                second_curr = check_value(second_curr)
                                if second_curr:
                                    if second_curr <= 4:
                                        print(f'''Введіть к-сть {currencies[first_curr]['name']}: ''')
                                        loop_three = True
                                        while loop_three:
                                            count_curr = input()
                                            count_curr = check_value(count_curr)
                                            if count_curr:
                                                result = (currencies[first_curr]['points'] / currencies[second_curr][
                                                    'points']) * count_curr
                                                result = round(float(result), 2)
                                                print(
                                                    f'''{count_curr} {currencies[first_curr]['name']} = {result} {currencies[second_curr]['name']}''')
                                                loop_three = False
                                                loop_two = False
                                                loop_one = False
                                else:
                                    print('Введіть номер від 1 до 4:')

                        else:
                            print('Введіть номер від 1 до 4:')
            elif task == 5:
                print('Завдання 5. Підкидання монети.')
                print('Введіть "heads" або "tails": ')
                variants = ['heads', 'tails']
                coin = random.choice(variants)
                loop_one = True
                while loop_one:
                    choice = input()
                    count = [1, 2, 3]
                    if choice:
                        choice = choice.lower()
                        if choice in variants:
                            for i in reversed(count):
                                print(i)
                                time.sleep(1)
                            if choice == coin:
                                print(f'{coin} - ви виграли!')
                                loop_one = False
                            else:
                                print(f'{coin} - ви програли!')
                                loop_one = False
                        else:
                            print(f'Ви ввели {choice}. Введіть "heads" або "tails": ')
            else:
                print('Не коректний номер')
        elif task == 'end':
            print('Завершення програми!')
            break
        else:
            print(f'Ви ввели {task}!')


if __name__ == '__main__':
    main()
