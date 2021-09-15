import json


def load_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def save_json(file_name, db):
    with open(file_name, 'w') as file:
        file.write(json.dumps(db))
        print('Файл бази даних, успішно оновлено')


def show_product(db):
    for category in db:
        print(f'        {category}')
        print('----------------------------')
        for product in db[category]:
            print(f'''{product}  ціна: {db[category][product]['price']}  залишок: {db[category][product]['count']}''')
        print()


def yes_or_no():
    print('Введіть "так"(т) або "ні"(н): ')
    loop = True
    while loop:
        choice = input()
        choice = choice.lower()
        if choice == 'так' or choice == 'т':
            return True
        elif choice == 'ні' or choice == 'н':
            return False
        else:
            print('Не коректна відповідь. Спробуйте ще раз!')


def validate_none():
    loop = True
    while loop:
        value = input()
        if value:
            return value
        else:
            print(f'Ви ввели порожнє значення. Спробуйте ще раз!')
            continue


def validate_digit(only_int=False, max_discount=False, max_count=0):
    loop = True
    while loop:
        value = input()
        if value.isdigit():
            print(f'''Ви ввели число - {value}''')
            if max_discount:
                if int(value) > 5:
                    print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                    continue
            if max_count:
                if int(value) > max_count:
                    print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                    continue
            return int(value)
        elif only_int:
            print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
            continue
        elif '-' in value or '.' in value or ',' in value:
            if '-' in value:
                value = value.replace('-', '')
                if value.isdigit():
                    print(f'''Ви ввели число - {value}''')
                    return int(value)
            if '.' in value or ',' in value:
                try:
                    if ',' in value:
                        value = value.replace(',', '.')
                    return float(value)
                except ValueError:
                    print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
                    continue
        else:
            print(f'Ви ввели некоректне значення - {value}. Спробуйте ще раз!')
            continue


def validate_section(for_discount=False):
    global DB
    loop = True
    while loop:
        value = input()
        if value:
            if value in DB:
                return value
            #  Ось тут в мене є питання щодо гарних манер. Заради перевикористання функції, добавленні наступні
            #  два рядки та параметр. Аналогічно наступна функція validate_product. Або дописати по два рядки коду,
            #  чим ускладнити її читання. Або створювати нову зліплену з цих двох функцій чим відкидуємо принцип
            #  перевикористання(принаймні наполовину, так як це не просто перевикористання, а й адаптація під
            #  перевикористання).
            #  Що буде правильнішим?? (так само адаптував validate_digit)
            elif for_discount:
                return False
            else:
                print(f'Ви ввели некоректний розділ - {value}. Спробуйте ще раз!')
                continue


def validate_product(for_discount=False):
    global DB
    loop = True
    while loop:
        value = input()
        if value:
            for section in DB:
                if value in DB[section]:
                    return value, section
                elif for_discount:
                    return False
                else:
                    continue
            print(f'Ви ввели некоректну назву товару - {value}. Спробуйте ще раз!')


def del_product(section, product, count):
    available_count = DB[section][product]['count']
    DB[section][product]['count'] = available_count - count
    save_json('market.json', DB)


def add_product():
    global DB
    print('Добавити новий товар')
    print('Доступні розділи: ', end='')
    for i in DB:
        print(f'{i} ', end='')
    print('\nВведіть розділ до якого відноситься новий товар:')
    section = validate_section()
    print('Введіть назву:')
    name = validate_none()
    print('Введіть ціну:')
    price = validate_digit()
    print('Введіть к-сть:')
    count = validate_digit(True)
    print(f'{name} {price} {count}')
    DB[section].update({name: {
                        'price': price,
                        'count': count}})
    print(f'Іспішно добавлено новий товар {name} в розділ {section}. Ціна - {price}, к-сть - {count}')
    save_json('market.json', DB)


def buy_product():
    global DB
    print('Придбати товар')
    print('Введіть назву товару:')
    product, section = validate_product()
    print(f'''Ви обрали {product}.''')
    print(f'''Ціна: {DB[section][product]['price']}. Залишок на складі: {DB[section][product]['count']}''')
    print('Введіть скільки товару хочете придбати.:')
    price = DB[section][product]['price']
    count = validate_digit(True, True, int(DB[section][product]['count']))
    print('Застосувати знижку?')
    choice = yes_or_no()
    if choice:
        print('Введіть відсоток вашої знижки. Максимум 5%')
        persent = validate_digit(True, True)
        discount = price / 100 * persent
        print(f'Ви придбали {product}. К-сть - {count}. Сума до оплати - {float(round((price-discount) * count, 2))}$')
    else:
        print(f'Ви придбали {product} в кількості - {count}. Сума до оплати - {float(round(price * count, 2))}$')
    del_product(section, product, count)


def show_discount():
    global DB
    print('Знижка')
    loop = True
    while loop:
        print('Введіть відсоток вашої знижки. Максимум 5%')
        percent = validate_digit(True, True)
        print('Введіть назву товару або розділу:')
        section = validate_section(True)
        if section:
            for product in DB[section]:
                price = DB[section][product]['price']
                discount = price / 100 * percent
                print(f'Ціна на товар {product} з урахуванням знижки {float(round((price-discount), 2))}$')
            break
        else:
            product, section = validate_product(True)
            if product:
                price = DB[section][product]['price']
                discount = price / 100 * percent
                print(f'Ціна на товар {product} з урахуванням знижки {float(round((price-discount), 2))}$')
                break
            else:
                print(f'Ви ввели некоректну назву. Спробуйте ще раз!')
                continue


DB = {}


def main():
    global DB
    DB = load_json('market.json')
    main_loop = True
    while main_loop:
        show_product(DB)
        print('-------------------------------------')
        print('')
        print('1. Добавити товар(add, a)')
        print('2. Купити товар(buy, b)')
        print('3. Показати товари з урахуванням знижки(discount, d)')
        print('Будь ласка введіть номер 1 - 3, або "end(enter)" для завершення програми: ')
        task = input()
        if task == '1' or task == 'add' or task == 'a':
            add_product()
        elif task == '2' or task == 'buy' or task == 'b':
            buy_product()
        elif task == '3' or task == 'discount' or task == 'd':
            show_discount()
        elif task == 'end' or task == '':
            print('Завершення програми!')
            break
        else:
            print('error')


if __name__ == '__main__':
    main()
