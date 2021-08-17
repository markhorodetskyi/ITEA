n = 'foo'
m = n
m = 'f1'
print(n, m)
print(type(n))
print(id(n), id(m))
print('-------------')

# -----------------------------------
name = 'mark'
x, y = 7, 4

_sum = x + y
print(f'name: {name}, sum: {_sum}')
print('-------------')

# -----------------------------------
x = 1
if x:
    print('''It's True''')
print('-------------')

# -----------------------------------
my_str_var = 'My new string'
print(my_str_var[3])
new_str = my_str_var + ' wow'
print(new_str)
x = '1' + '1'
x = x * 3
print(x)
for element in my_str_var:
    print(element + ' 1')
if 'new' in my_str_var:
    print('yes')
print('-------------')

# -----------------------------------
# x = input('Enter number pls.. ')
# print(type(x))
print('-------------')

# -----------------------------------
my_dict = {'name': 'mark', 'last_name': 'horodetskyi'}
for key, value in my_dict.items():
    print(f'key: {key}, value: {value}')
my_dict.update({'age': '30'})
print(my_dict)
print('-------------')

# -----------------------------------
x = 1
y = '1'
print(type(str(x)), type(y))
print(str(x), y)
print(id(str(x)), id(y))
print(str(x) is y)
print('-------------')

# -----------------------------------
# my_input = input('Please enter only number ..')
# if my_input.isdigit():
#     x = int(my_input) + 1
# else:
#     print('Its not number')
# print(my_input)
# print('-------------')

# -----------------------------------
in_name = input('Please enter your name:')
print(f'Welcome ,{in_name}!')
digits1 = input('Please enter first number:')
if digits1.isdigit():
    pass
else:
    print('Its not number')
digits2 = input('Please enter second number:')
if digits2.isdigit():
    pass
else:
    print('Its not number')
print(f'Sum two numbers - {digits1+digits2}!')