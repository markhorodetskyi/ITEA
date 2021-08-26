print('   Завдання 1')
my_tuple = ('abc', 25, '32')
for i in my_tuple:
    if isinstance(i, int):
        print(f'{i} - це число')
print('')
print('   Завдання 2')

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
print('')
print('   Завдання 3')
x = ['d', 'a', 'w', 'i', 's', 'd', 'a']
print(set(x))

print('')
print('   Завдання 4')
my_list2 = [1, 5, -6, 8, 0, -2, -4]
del_items = my_list2.copy()
list_sum = 0
for i in my_list2:
    if i <= 0:
        print(f'''Знайдено від`ємне число - {i}''')
        del_items.remove(i)
    else:
        list_sum = list_sum + i
print(del_items)
print(f'Сума всіх додатніх чисел - {list_sum}')

print('')
print('   Завдання 5')
my_dict = {0: 'London',
           1: 'New-York',
           2: 'Berlin'}
print(f'Дано словник - {my_dict}')
print(f'Значення - {list(my_dict.values())}')
print(f'Ключі - {list(my_dict.keys())}')
print('')
new_dict = {value: key for key, value in my_dict.items()}
print(f'Ключі та значення міняємо місцями - {new_dict}')

print('')
print('   Завдання 6')
int_list = [2, 5, 1, 7, 9, 3, 4]
min = 999
for i in int_list:
    if i < min:
        min = i
print(f'Мінімальне число - {min}')

print('')
print('   Завдання 7')
str_list = ['abddc', 'vkhfgtr', 'ckjjfdnc', 'dkfjd', 'coroc']
for i in str_list:
    if i[0] == i[-1]:
        print(f'{i}')

print('')
print('   Завдання 8')
new_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict_copy = new_dict.copy()
for key, value in new_dict.items():
    if value == None:
        new_dict_copy.pop(key)
print(new_dict_copy)

print('')
print('   Завдання 9')
new_dict = {'c1': 'Red', 'c2': 'Green', 'c3': 'abracadabra'}
inp = input('Введіть ключ: ')
for key in new_dict:
    if key == inp:
        print('Такий ключ існує')

print('')
print('   Завдання 10')
new_dict = {'c1': 'Red', 'c2': 'Green', 'c3': 'abracadabra'}
new_dict_copy = new_dict.copy()
inp = input('Введіть ключ: ')
for key in new_dict:
    if key == inp:
        new_dict_copy.pop(key)
print(new_dict_copy)