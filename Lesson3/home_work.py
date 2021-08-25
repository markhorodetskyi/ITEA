import random
import string
import secrets


class Manipulation:
    def __init__(self, stroke):
        self.stroke = stroke

    def check_none(self):
        if self.stroke:
            print(f'Ви ввели "{self.stroke}"')
            return True
        else:
            print('Ви нічого не ввели!')
            return False

    def yes_or_no(self):
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

    def to_lower(self):
        return self.stroke.lower()

    def count_vowels(self):
        return ''.join(s for s in self.stroke if s in 'aoyeuiAOYEUI')

    def count_consonant(self):
        return ''.join(s for s in self.stroke if s not in 'aoyeuiAOYEUI')

    def reverse(self):
        reverse_up_low = ''
        for letter in self.stroke:
            if letter.isupper():
                reverse_up_low = reverse_up_low + letter.lower()
            else:
                reverse_up_low = reverse_up_low + letter.upper()
        return reverse_up_low

    def get_domain(self):
        low_loop = True
        castom_stroke = ''
        while low_loop:
            if castom_stroke:
                low_stroke = castom_stroke.lower()
            else:
                low_stroke = self.to_lower()
            www = low_stroke.find('www.')
            http = low_stroke.find('://')
            if www > (-1):
                print(1)
                dot = low_stroke[www+4:].find('.')
                new_stroke = low_stroke[www+4:]
                low_loop = False
                return new_stroke[:dot]
            elif http > -1:
                print(2)
                dot = low_stroke[http + 3:].find('.')
                new_stroke = low_stroke[http + 3:]
                low_loop = False
                return new_stroke[:dot]
            else:
                print('В рядку немає URL адреси, ввести її зараз?')
                if self.yes_or_no():
                    castom_stroke = input('Введіть URL адресу: ')
                else:
                    low_loop = False

    def is_lower(self):
        if self.stroke.islower():
            return 'Всі символи в стрічці в нижньому реєстрі'
        else:
            for letter in self.stroke:
                if letter.isupper():
                    print(f'Літера {letter.lower()} у верхньому реєстрі')

    def password(self, size):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(size, 12))



def main():
    main_loop = True
    while main_loop:
        print('-------------------------------------')
        print('')
        print('1. Завдання 1-4. Маніпуляції з рядком.')
        print('2. Генератор паролів.')
        print('Будь ласка введіть номер 1 - 2, або "end" для завершення програми: ')
        task = input()
        if task.isdigit():
            task = int(task)
            if task == 1:
                print('Будь ласка введіть будь яку стрічку: ')
                stroke = Manipulation(input())
                if stroke.check_none():
                    low_loop = True
                    while low_loop:
                        print('')
                        print('1. Вивести к-сть голосних букв.')
                        print('2. Вивести к-сть приголосних букв.')
                        print('3. Перевести малі літери у великі та навпаки.')
                        print('''4. Вивести домене ім'я з URL адреси.''')
                        print('5. Вивести всі літери, які знаходяться у верхньому реєстрі.')
                        print('6. Перевести всі літери у нижній реєстр.')
                        print('7. Перевести всі літери у верхній реєстр.')
                        print('Будь ласка введіть: ')
                        print('  номер операції 1 - 5')
                        print('  "back" для повернення в попереднє меню')
                        print('  "end" для завершення програми')
                        low_task = input()
                        if low_task.isdigit():
                            low_task = int(low_task)
                            if low_task == 1:
                                print(f'{stroke.stroke} - містить {len(stroke.count_vowels())} голосних букв({stroke.count_vowels()})')
                            if low_task == 2:
                                print(f'{stroke.stroke} - містить {len(stroke.count_consonant())} приголосних букв({stroke.count_consonant()})')
                            if low_task == 3:
                                print(f'{stroke.stroke}, навпаки - "{stroke.reverse()}"')
                            if low_task == 4:
                                print(f'''Домене ім'я введеного URL - "{stroke.get_domain()}"''')
                            if low_task == 5:
                                print(stroke.is_lower())
                            if low_task == 6:
                                print(f'{stroke.stroke.lower()} - рядок з літерами у нижньому реєестрі')
                            if low_task == 7:
                                print(f'{stroke.stroke.upper()} - рядок з літерами у верхньому реєестрі')
                        elif low_task == 'back':
                            low_loop = False
                            continue
                        elif low_task == 'end':
                            print('Завершення програми!')
                            break
                else:
                    continue

            elif task == 2:
                low_loop = True
                while low_loop:
                    print('')
                    print('Будь ласка введіть довжину паролю 8-16 символів: ')
                    size = input()
                    if not size:
                        print('Ви нічого не ввели! Спробуйте ще раз')
                        continue
                    if size.isdigit():
                        size = int(size)
                        if size >=8 and size <=16:
                            chars = (string.ascii_uppercase, string.ascii_lowercase, string.digits)
                            print(f'''Ваш новий пароль - "{''.join(secrets.choice(secrets.choice(chars)) for x in range(0, size))}"''')
                            low_loop = False
                        else:
                            print('Невірна к-сть символів! Спробуйте ще раз')
                            continue
        elif task == 'end':
            print('Завершення програми!')
            break


if __name__ == '__main__':
    main()
