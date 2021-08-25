import string

print('Завдання 1')
my_str_1 = 'hello'
my_str_1 = my_str_1[::-1]
print(my_str_1)

print('Завдання 2')
my_str_2 = input('Введіь будь яку стрічку: ')
print(f'Після видалення першого і останнього символу, стрічка виглядає так: {my_str_2[1:-1]}')

print('Завдання 3')
my_str_3 = input('Введіь будь яку стрічку: ')
letter_one = my_str_3[:1]
letter_two = my_str_3[-1:]
print(f'{letter_two}{my_str_3[1:-1]}{letter_one}')

print('Завдання 4')
my_str_4 = 'HeLLo My naMe is jack'
my_str_4 = my_str_4.lower().capitalize()
my_str_4 = my_str_4.split(' ')
my_str_4[4] = my_str_4[4].capitalize()
my_str_4 = ' '.join(my_str_4)
print(my_str_4)

print('Завдання 5')
print(''.join(s for s in my_str_4 if s != ' '))


print('Завдання 6')
my_str_6 = 'HelloWorlD'
print(f'{my_str_6[:5]} {my_str_6[5:].lower().capitalize()}')

print('Завдання 7')
print(''.join(s for s in 'amazing' if s not in 'aoyeui'))

print('Завдання 8')
loop = True
while loop:
    my_str_8 = input('Введіь нікнейм: ')
    if len(my_str_8) > 16 or len(my_str_8) < 4:
        print('довжина нікнейму повинна бути в межах 4-16 символів')
        continue
    for digits in string.digits:
        if digits in my_str_8:
            print('Нікнейм не повиненм містити цифри')
            continue
    for symb in string.punctuation:
        if symb in my_str_8:
            print('Нікнейм не повиненм містити спец.символи')
            continue
    print(f'Ваш нікнейм: {my_str_8}')
    loop = False