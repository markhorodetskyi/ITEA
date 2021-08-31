import random


def verify_sort():
    sort_list = []
    while len(sort_list) < 10:
        sort_list.append(random.randint(1, 100))
    if random.choice([True, False]):
        pass
    else:
        sort_list.sort()
    print(f'Згенеровано масив - {sort_list}')
    if sort_list == sorted(sort_list):
        print('Масив є відсортований!')
    else:
        print('Масив НЕ є відсортований!')


def list_sum():
    sort_list = []
    multiply_list = 1
    print('Потрібно ввести 10 чисел. Будь ласка введіть перше:')
    while len(sort_list) < 10:
        digit = input()
        print(f'Ви ввели - {digit}')
        try:
            digit = int(digit)
            sort_list.append(digit)
            if digit > 0:
                multiply_list = multiply_list * digit
        except ValueError:
            print('Ви ввели не число, спробуйте ще раз')
            continue
        if len(sort_list) < 9:
            print('Введіть наступне число: ')
        elif len(sort_list) == 9:
            print('Введіть останнє число: ')

    print(f'Створений список - {sort_list}')
    print(f'Добуток всіх додатніх чисел - {multiply_list}')


def reverse_list():
    words = []
    reverse_words = []
    print('Потрібно ввести 5 слів. Будь ласка введіть перше:')
    while len(words) < 5:
        inp = input()
        words.append(inp)
        reverse_words.append(inp[::-1])
        if len(words) < 4:
            print('Введіть наступне слово: ')
        elif len(words) == 4:
            print('Введіть останнє слово: ')
    print(f'Створений список - {words}')
    print(f'Перевернуті слова - {reverse_words}')


def most_expensive():
    goods = {'Sugar': 3,
             'Salt': 1.5,
             'Black Pepper': 2.5,
             'Paprika': 2.5,
             'Chili Pepper': 3.2,
             'Anise': 4,
             'Cinnamon': 5}
    prices = list(goods.values())
    while len(prices) > 3:
        prices.remove((min(prices)))
    print('Три найдорожчих товари: ')
    for key, values in goods.items():
        if values in prices:
            print(f'Назва: {key}, ціна - {values} UAH')


def search_hotel():
    hotels = {'Continental Hotel': '****',
             'Big Street Hotel': '**',
             'Corner Hotel': '**',
             'Trashviews Hotel': '*',
             'Hazbins': '****',
             'Hazbins Deluxe': '*****',
             'Arkadia': '***',
             'Dolphin': '*****'}
    loop = True
    while loop:
        print('Введіть к-сть зірок: ')
        stars = input()
        if stars.isdigit():
            for key, value in hotels.items():
                if len(value) == int(stars):
                    print(key)
            loop = False
        else:
            print('Ви ввели не число, спробуйте ще раз')


def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('1. Завдання 1. Чи відсортований список?')
        print('2. Завдання 2. Сума всіх додатніх чисел у списку')
        print('3. Завдання 3. Перевернуті рядки в списку')
        print('4. Завдання 4. Три найдорожчі товари')
        print('5. Завдання 5. Готелі')
        print('Будь ласка введіть номер 1 - 5, або "end" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                verify_sort()
            elif task == 2:
                list_sum()
            elif task == 3:
                reverse_list()
            elif task == 4:
                most_expensive()
            elif task == 5:
                search_hotel()
        elif task == 'end':
            print('Завершення програми!')
            break


if __name__ == '__main__':
    main()
